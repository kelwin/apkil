#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import copy

from logger import log

INSN_FMT = {
        "invoke-virtual": "35c",
        "invoke-super": "35c",
        "invoke-direct": "35c",
        "invoke-static": "35c",
        "invoke-interface": "35c"
        }

BASIC_TYPES = {
        'V': "void",
        'Z': "boolean",
        'B': "byte",
        'S': 'short',
        'C': "char",
        'I': "int",
        'J': "long",
        'F': "float",
        'D': "double"
        }

class SmaliTree(object):

    def __init__(self, foldername):
        self.foldername = ""
        self.smali_files = []
        self.classes = []

        self.__parse(foldername)

    def __repr__(self):
        return "Foldername: %s\n%s" % \
                (self.foldername, \
                "".join([repr(class_) for class_ in self.classes]))

    def __parse(self, foldername):
        self.foldername = foldername
        for (path, dirs, files) in os.walk(self.foldername):
            for f in files:
                name = os.path.join(path, f)
                ext = os.path.splitext(name)[1]
                if ext != '.smali': continue
                self.smali_files.append(name)
                self.classes.append(ClassNode(name))
        # print repr(self.smali_files)
        log("SmaliTree parsed!")

    def get_class(self, class_name):
        result = [c for c in self.classes if c.name == class_name]
        if result:
            return result[0]
        else:
            return None
    
    def add_class(self, class_node):
        if [c for c in self.classes if c.name == class_node.name]:
            print "Class %s alreasy exsits!" % class_node.name
            return False
        else:
            self.classes.append(copy.deepcopy(class_node))
            return True

    def remove_class(self, class_node):
        # self.classes.del()
        pass

    def save(self, new_foldername):
        if not os.path.exists(new_foldername):
            os.makedirs(new_foldername)
        for c in self.classes:
            c.save(new_foldername)

    def export_apk(self):
        self.save("./out")

    def get_insn35c(self, opcode_name, method_desc):
        result = []
        for c in self.classes:
            result.extend(c.get_insn35c(opcode_name, method_desc))
        return result


class ClassNode(object):

    def __init__(self, filename=None):
        self.buf = []
        self.filename = "" 
        self.name = ''
        self.super_name= ''
        self.source = ''
        self.access = []
        self.interfaces = []
        self.fields = []
        self.methods = []
        self.inner_classes = []
        self.annotations = []
        self.debugs = []

        if filename:
            self.__parse(filename)

    def __repr__(self):
        return  "Class: %s %s << %s\n%s%s" % \
                (' '.join(self.access), self.name, self.super_name, \
                ''.join([repr(f) for f in self.fields]), \
                ''.join([repr(m) for m in self.methods]))

    def __parse(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        line = f.readline()
        while line:
            # print line
            if line.isspace():
                line = f.readline()
                continue
            line = line.strip()
            segs = line.split()
            # .source <source-file>
            if segs[0] == ".source":
                self.source = segs[1]
            # .class <access-spec> <class-name>
            elif segs[0] == ".class":
                self.name = segs[-1]
                # <access-spec>: public, final, super, interface, abstract
                self.access = segs[1:-1]
            # .super <class-name>
            elif segs[0] == ".super":
                self.super_name = segs[1]
            elif segs[0] == ".interface":
                pass
            elif segs[0] == ".implements":
                pass
            elif segs[0] == ".field":
                self.fields.append(FieldNode(line))
            elif segs[0] == ".method":
                lines = [line]
                line = f.readline()
                while line:
                    if line.isspace():
                        line = f.readline()
                        continue
                    line = line.strip()
                    lines.append(line)
                    segs = line.split(None, 2)
                    if segs[0] == ".end" and segs[1] == "method":
                        break
                    line = f.readline()
                self.methods.append(MethodNode(lines))
            elif segs[0] == ".annotation":
                pass
            elif segs[0] == '#':
                pass
            line = f.readline()
        f.close()
        log("ClassNode: " + self.name + " parsed!")

    def reload(self):
        self.buf = []
        # .class
        self.buf.append(".class %s %s" % (' '.join(self.access), self.name))
        # .super
        self.buf.append(".super %s" % (self.super_name, ))
        # .source
        # self.buf.append(".source %s" % (self.source, ))
        # .field
        for f in self.fields:
            f.reload()
            self.buf.append(f.buf)
        # .method
        for m in self.methods:
            m.reload()
            self.buf.extend(m.buf)

    def set_name(self, name):
        self.name = name
    
    def set_super_name(self, super_name):
        self.super_name = super_name
    
    def add_field(self, field):
        self.fields.append(field)

    def add_method(self, method):
        if type(method) == list:
            self.methods.extend(method)
        else:
            self.methods.append(method)

    def save(self, new_foldername):
        self.reload()
        path, filename = os.path.split(self.name[1:-1])
        filename += ".smali"
        path = os.path.join(new_foldername, path)
        if not os.path.exists(path):
            os.makedirs(path)
        filename = os.path.join(path, filename)
        f = open(filename, 'w')
        f.write('\n'.join(self.buf))
        f.close()

    def get_insn35c(self, opcode_name, method_desc):
        result = []
        for m in self.methods:
            result.extend(m.get_insn35c(opcode_name, method_desc))
        return result

class FieldNode(object):

    def __init__(self, line=None):
        self.buf = ""
        self.name = ""
        self.access = []
        self.descriptor = ""
        self.value = None

        if line:
            self.__parse(line)

    def __repr__(self):
        return "    Field: %s %s %s%s\n" % \
                (' '.join(self.access), self.descriptor, self.name, \
                self.value and "=" + self.value or "")

    # .field <access-spec> <field-name>:<descriptor> [ = <value> ]
    def __parse(self, line):
        self.buf = line
        segs = self.buf.split()
        if segs[-2] != '=':
            self.access = segs[1:-1]
            self.name, self.descriptor = segs[-1].split(':')
        else:
            self.access = segs[1:-3]
            self.name, self.descriptor = segs[-3].split(':')
            self.value = segs[-1]
        log("FieldNode: " + self.name + " parsed!")

    def set_name(self, name):
        self.name = name


    def add_access(self, access):
        if type(access) == list:
            self.access.extend(access)
        else:
            self.access.append(access)

    def set_desc(self, desc):
        self.descriptor = desc

    def set_value(self, value):
        self.value = value
    
    def reload(self):
        self.buf = "%s %s %s:%s" % \
                (".field", ' '.join(self.access), self.name, \
                self.descriptor)
        if self.value: self.buf += " = %s" % self.value

class MethodNode(object):

    def __init__(self, lines=None):
        self.name = ""
        self.buf = []
        self.access = []
        self.descriptor = ""
        self.paras = []
        self.ret = ""
        self.registers = 0
        self.insns = []
        self.labels = {}
        self.tries = []
        self.is_constructor = False

        if lines:
            self.__parse(lines)


    def __repr__(self):
        return "    Method: %s %s\n        registers: %d\n%s" % \
                (' '.join(self.access), self.descriptor, self.registers, \
                ''.join(["%13d %s" % \
                (self.insns.index(i), repr(i)) for i in self.insns]))

    # .method <access-spec> <method-spec>
    #     <statements>
    # .end method
    def __parse(self, lines):
        self.buf = lines
        segs = self.buf[0].split()
        self.access = segs[1:-1]
        self.descriptor = segs[-1]
        self.__parse_desc()

        start = 1
        # .registers <register-num>
        segs = self.buf[1].split()
        if segs[0] == ".registers":
            self.registers = int(segs[1])
            start = 2

        index = 0
        try_node_cache = []
        for line in self.buf[start:-1]:
            segs = line.split()
            # :<label-name>
            if segs[0][0] == ":":
                label = LabelNode(line, index)
                self.labels[label.name] = label
            # .catch <classname> {<label1> .. <label2>} <label3>
            # .catchall {<label1> .. <label2>} <label3>
            elif segs[0][0] == '.' and \
                    (segs[0][1:] == "catch" or segs[0][1:] == "catchall"):
                try_node_cache.append(line)
            else:
                self.insns.append(InsnNode(line))
                index += 1

        for line in try_node_cache:
            segs = line.split()
            start = self.labels[segs[-4][2:]]
            end = self.labels[segs[-2][1:-1]]
            handler = self.labels[segs[-1][1:]]
            self.tries.append(TryNode(line, start, end, handler))
        try_node_cache = []

        if self.name == "<init>":
            self.is_constructor = True
        log("MethodNode: " + self.name + " parsed!")

    def __parse_desc(self):
        print "@@"+self.descriptor
        self.name = self.descriptor.split('(', 1)[0]
        p1 = self.descriptor.find('(')
        p2 = self.descriptor.find(')')
        self.ret = TypeNode(self.descriptor[p2 + 1:])
        self.paras = []
        paras = self.descriptor[p1 + 1:p2]
        index = 0
        dim = 0
        while index < len(paras):
            c = paras[index]
            if c == '[':
                dim += 1
                index += 1
            elif BASIC_TYPES.has_key(c):
                self.paras.append(TypeNode(paras[index - dim:index + 1]))
                index += 1
                dim = 0
            else:
                tmp = paras.find(';', index)
                self.paras.append(TypeNode(paras[index - dim:tmp + 1]))
                index = tmp + 1
                dim = 0

    def reload(self):
        self.__parse_desc()

        self.buf = []
        for i in self.insns:
            i.reload()
            self.buf.append(i.buf)
        # insert labels and tries
        # sort the labels by index
        count = 0
        labels = self.labels.values()
        from operator import attrgetter
        labels = sorted(labels, key=attrgetter('index'))
        for l in labels:
            self.buf.insert(l.index + count, l.buf)
            count += 1
            for t in l.tries:
                self.buf.insert(l.index + count, t.buf)
                count += 1

        if self.registers > 0:
            self.buf.insert(0, ".registers %d" % self.registers)
        self.buf.insert(0, ".method %s %s" % \
                (' '.join(self.access), self.descriptor))
        self.buf.append(".end method")

    def get_insn_by_index(self, index):
        if index < 0 or index >= len(self.insns): return None
        return self.insns[index]

    def get_insn35c(self, opcode_name, method_desc):
        result = []
        for i in self.insns:
            if i.fmt == "35c" and i.opcode_name == opcode_name and \
                    i.obj.method_desc == method_desc:
                result.append(i)
        return result

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.descriptor = desc
        self.__parse_desc()

    def add_para(self, para, index=0):
        self.paras.insert(index, para)
        self.descriptor = self.name + '('
        for p in self.paras:
            self.descriptor += p.get_desc()
        self.descriptor += ')'
        self.descriptor += self.ret.get_desc()

    def add_access(self, access):
        if type(access) == list:
            self.access.extend(access)
        else:
            self.access.append(access)

    def set_registers(self, registers):
        self.registers = registers

    def add_insn(self, insn):
        if type(insn) == list:
            self.insns.extend(insn)
        else:
            self.insns.append(insn)

    def add_label(self, label):
        pass

    def replace_insn35c(self):
        for i in self.insns:
            i.replace()
    

class InsnNode(object):

    def __init__(self, line=None):
        self.buf = ""
        self.opcode_name = ""
        self.fmt = ""
        self.obj = None

        if line:
            self.__parse(line)

    def __repr__(self, line_number=""):
        return "%s\n" % \
                (self.buf, )

    def __parse(self, line):
        self.buf = line
        segs = self.buf.split()
        self.opcode_name = segs[0] 
        if INSN_FMT.has_key(self.opcode_name):
            self.fmt = INSN_FMT[self.opcode_name]

        if self.fmt == "35c":
            self.obj = Insn35c(line)

        log("InsnNode: " + self.opcode_name + " parsed!")

    def reload(self):
        if self.obj:
            self.obj.reload()
            self.buf = self.obj.buf
        else:
            pass


class TryNode(object):

    def __init__(self, line, start, end, handler):
        self.buf = "" 
        self.exception = ""
        self.start = None
        self.end = None
        self.handler = None

        self.__parse(line, start, end, handler)

    def __repr__(self):
        return "Try: %s {%s .. %s} %s" % \
                (self.exception, start.index, end.index, handler.index)

    def __parse(self, line, start, end, handler):
        self.buf = line
        self.start = start
        self.end = end
        end.tries.append(self)
        self.handler = handler
        segs = self.buf.split()
        self.exception = segs[1]

    def reload(self):
        pass

class LabelNode(object):

    def __init__(self, line, index):
        self.name = ""
        self.buf = ""
        self.index = -1
        self.tries = []

        self.__parse(line, index)

    def __repr__(self):
        return "Lable: %s\n" % \
                (self.name, )

    def __parse(self, line, index):
        self.buf = line
        self.index = index
        self.name = self.buf[1:]

        log("LabelNode: " + self.name + " parsed!")

    def reload(self):
        pass

class Insn35c(object):

    def __init__(self, line):
        self.buf = ""
        self.opcode_name = ""
        self.registers = []
        self.method_descriptor = ""

        self.__parse(line)

    def __repr__(self):
        return "%s\n" % self.buf

    def __parse(self, line):
        self.buf = line
        tmp = self.buf
        tmp = tmp.replace('{', '')
        tmp = tmp.replace('}', '')
        tmp = tmp.replace(',', '')
        segs = tmp.split()
        self.opcode_name = segs[0]
        self.registers = segs[1:-1]
        self.method_desc = segs[-1]

    def reload(self):
        self.buf = "%s {%s}, %s" % \
                (self.opcode_name, ", ".join(self.registers), \
                self.method_desc)

    def replace(self, opcode_name, method_desc):
        self.opcode_name = opcode_name
        self.method_desc = method_desc


class TypeNode(object):

    def __init__(self, desc):
        print "***"+desc
        self.type_ = ""
        self.dim = 0
        self.basic = None
        self.void = None

        self.__parse(desc)

    def __parse(self, desc):
        self.dim = desc.rfind('[') + 1
        desc = desc[self.dim:]

        if BASIC_TYPES.has_key(desc[0]):
            self.type_ = desc[0]
            self.basic = True
            if self.type_ == 'V':
                self.void = True
            else:
                self.void = False
        elif desc[0] == 'L':
            self.type_ = desc
            self.basic = False

    def __repr__(self):
        return self.dim * '[' + self.type_

    def get_desc(self):
        return self.dim * '[' + self.type_

    def get_java(self):
        if self.basic:
            if self.void:
                return ""
            else:
                return BASIC_TYPES[self.type_] + self.dim * "[]"
        else:
            return self.type_[1:-1].replace('/', '.') + self.dim * "[]"
