#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from logger import log

INSN_FMT = {
        "invoke-virtual": "35c",
        "invoke-super": "35c",
        "invoke-direct": "35c",
        "invoke-static": "35c",
        "invoke-interface": "35c"
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

    def save(self, new_foldername):
        if not os.path.exists(new_foldername):
            os.makedirs(new_foldername)
        for c in self.classes:
            c.save(new_foldername)

    def export_apk(self):
        self.save("./out")
        pass


class ClassNode(object):

    def __init__(self, filename):
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
        self.buf.extend([f.buf for f in self.fields])
        # .method
        for m in self.methods:
            self.buf.extend(m.buf)

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


class FieldNode(object):

    def __init__(self, line):
        self.buf = ""
        self.name = ""
        self.access = []
        self.descriptor = ""
        self.value = None

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
    
    def reload(self):
        self.buf = "%s %s %s:%s" % \
                (".field", ' '.join(self.access), self.name, \
                self.descriptor)
        if self.value: self.buf += " = self.value"

class MethodNode(object):

    def __init__(self, lines):
        self.name = ""
        self.buf = []
        self.access = []
        self.descriptor = ""
        self.registers = 0
        self.insns = []
        self.labels = {}
        self.tries = []

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
        self.name = self.descriptor.split('(', 1)[0]

        # .registers <register-num>
        segs = self.buf[1].split()
        # segs[0] == ".registers"
        self.registers = int(segs[1])

        index = 0
        try_node_cache = []
        for line in self.buf[2:-1]:
            segs = line.split()
            # :<label-name>
            if segs[0][0] == ":":
                label = LabelNode(line, index)
                self.labels[label.name] = label
            # .catch <classname> {<label1> .. <label2>} <label3>
            elif segs[0][0] == '.' and segs[0][1:] == "catch":
                try_node_cache.append(line)
            else:
                self.insns.append(InsnNode(line))
                index += 1

        for line in try_node_cache:
            segs = line.split()
            start = self.labels[segs[2][2:]]
            end = self.labels[segs[4][1:-1]]
            handler = self.labels[segs[-1][1:]]
            self.tries.append(TryNode(line, start, end, handler))
        try_node_cache = []

        log("MethodNode: " + self.name + " parsed!")

    def reload(self):
        pass
    

class InsnNode(object):

    def __init__(self, line):
        self.buf = ""
        self.opcode_name = ""
        self.fmt = ""
        self.obj = None

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

        log("InsnNode: " + self.opcode_name + " parsed!")

    def reload(self):
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
        self.registers = segs[1:-1]
        self.method_descriptor = segs[-1]

    def reload(self):
        pass
