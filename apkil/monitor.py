#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import copy

from logger import log
from smali import ClassNode, MethodNode, FieldNode, InsnNode, \
                  TypeNode, LabelNode, TryNode, SmaliTree

PKG_PREFIX = "droidbox"
DEFAULT_HELPER = \
r'''
.class public Ldroidbox/apimonitor/Helper;
.super Ljava/lang/Object;
.method public constructor <init>()V
.registers 1
invoke-direct {p0}, Ljava/lang/Object;-><init>()V
return-void
.end method
.method public static log(Ljava/lang/String;)V
.registers 3
const-string v0, "\n"
const-string v1, "\\\\n"
invoke-virtual {p0, v0, v1}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
move-result-object p0
const-string v0, "\r"
const-string v1, "\\\\r"
invoke-virtual {p0, v0, v1}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
move-result-object p0
const-string v0, "DroidBox"
invoke-static {v0, p0}, Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I
return-void
.end method
.method public static toString(Ljava/lang/Object;)Ljava/lang/String;
.registers 5
if-nez p0, :cond_5
const-string v3, "null"
:goto_4
return-object v3
:cond_5
invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;
move-result-object v3
invoke-virtual {v3}, Ljava/lang/Class;->isArray()Z
move-result v3
if-eqz v3, :cond_3e
new-instance v2, Ljava/lang/StringBuilder;
const-string v3, "["
invoke-direct {v2, v3}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
invoke-static {p0}, Ljava/lang/reflect/Array;->getLength(Ljava/lang/Object;)I
move-result v1
const/4 v0, 0x0
:goto_1b
if-lt v0, v1, :cond_27
const-string v3, "]"
invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
move-result-object v3
goto :goto_4
:cond_27
invoke-static {p0, v0}, Ljava/lang/reflect/Array;->get(Ljava/lang/Object;I)Ljava/lang/Object;
move-result-object v3
invoke-static {v3}, Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;
move-result-object v3
invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
add-int/lit8 v3, v1, -0x1
if-ge v0, v3, :cond_3b
const-string v3, ", "
invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
:cond_3b
add-int/lit8 v0, v0, 0x1
goto :goto_1b
:cond_3e
invoke-virtual {p0}, Ljava/lang/Object;->toString()Ljava/lang/String;
move-result-object v3
goto :goto_4
.end method
'''

class APIMonitor(object):

    def __init__(self, method_descs):
        self.method_descs = method_descs
        self.stub_classes = {}
        self.method_map = {}
        self.class_map = {}
        self.helper = ClassNode(buf=DEFAULT_HELPER)
        for m in method_descs:
            self.add_stub_method(m)

    def __repr__(self):
        pass

    def inject(self, smali_tree):
        st = copy.deepcopy(smali_tree)
        for api in self.method_descs:
            segs = api.split(':', 1)
            method_type = segs[0]
            api = segs[1]
            segs = api.split("->")
            if method_type == "constructor":
                for c in st.classes:
                    for m in c.methods:
                        for i in range(len(m.insns)):
                            insn = m.insns[i]
                            if insn.fmt == "35c" and \
                               insn.opcode_name == "invoke-direct" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static", \
                                        self.method_map[api])
                                r = insn.obj.registers.pop(0)
                                m.insert_insn(InsnNode(\
"move-result-object %s" % r), i + 1, 0)
                            if insn.fmt == "3rc" and \
                               insn.opcode_name == "invoke-direct/range" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static/range", \
                                        self.method_map[api])
                                r = insn.obj.reg_start
                                nr = r[0] + str(int(r[1:]) + 1)
                                insn.obj.set_reg_start(nr)
                                m.insert_insn(InsnNode(\
"move-result-object %s" % r), i + 1, 0)
            elif method_type == "instance":
                for c in st.classes:
                    for m in c.methods:
                        for i in range(len(m.insns)):
                            insn = m.insns[i]
                            if insn.fmt == "35c" and \
                               insn.opcode_name == "invoke-virtual" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static", \
                                        self.method_map[api])
                            if insn.fmt == "3rc" and \
                               insn.opcode_name == "invoke-virtual/range" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static/range", \
                                        self.method_map[api])
            elif method_type == "static":
                for c in st.classes:
                    for m in c.methods:
                        for i in range(len(m.insns)):
                            insn = m.insns[i]
                            if insn.fmt == "35c" and \
                               insn.opcode_name == "invoke-static" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static", \
                                        self.method_map[api])
                            if insn.fmt == "3rc" and \
                               insn.opcode_name == "invoke-static/range" and \
                               insn.obj.method_desc == api:
                                insn.obj.replace("invoke-static/range", \
                                        self.method_map[api])

        for c in self.stub_classes.values():
            st.add_class(c)

        st.add_class(self.helper)
        return st

    def add_stub_method(self, m):
        segs = m.split(':', 1)
        method_type = segs[0]
        m = segs[1]
        segs = m.rsplit("->", 1)

        if self.stub_classes.has_key(segs[0]):
            stub_class = self.stub_classes[segs[0]]
        else:
            stub_class = ClassNode()
            stub_class.set_name("L" + PKG_PREFIX + "/" + segs[0][1:])
            stub_class.add_access("public")
            stub_class.set_super_name("Ljava/lang/Object;")

            self.stub_classes[segs[0]] = stub_class
            self.class_map[segs[0]] = "L" + PKG_PREFIX + "/" + segs[0][1:]

            #.method public constructor <init>()V
            #    .registers 1
            #    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
            #    return-void
            #.end method
            method = MethodNode()
            method.set_desc("<init>()V")
            method.add_access(["public", "constructor"])
            method.set_registers(1)
            i1 = InsnNode("invoke-direct {p0}, Ljava/lang/Object;-><init>()V")
            i2 = InsnNode("return-void")
            method.add_insn([i1, i2])
            stub_class.add_method(method)

        method_name = segs[1][:segs[1].find("(")]
        if method_type == "constructor":
            self.__add_stub_cons(stub_class, m)
        elif method_type == "instance":
            self.__add_stub_inst(stub_class, m)
        elif method_type == "static":
            self.__add_stub_static(stub_class, m)


    def __add_stub_inst(self, stub_class, m):
        segs = m.rsplit("->", 1)

        method = MethodNode()
        method.set_desc(segs[1])
        method.add_para(TypeNode(segs[0]))
        method.add_access(["public", "static"])

        para_num = len(method.paras)
        reg_num = method.get_paras_reg_num()
        ri = 1

        if reg_num <= 5:
            i = "invoke-virtual {%s}, %s" % \
                    (", ".join(["p%d" % k for k in range(reg_num)]), m)
        else:
            i = "invoke-virtual/range {p0 .. p%d}, %s" % (opcode, reg_num - 1, m) 

        method.add_insn(InsnNode(i)) 

        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("move-result v1"))
                    ri += 1
                else:
                    method.add_insn(InsnNode("move-result-wide v1"))
                    ri += 2
            else:
                method.add_insn(InsnNode("move-result-object v1"))
                ri += 1

        method.add_insn(InsnNode("new-instance \
v%d, Ljava/lang/StringBuilder;" % ri))
        method.add_insn(InsnNode("invoke-direct \
{v%d}, Ljava/lang/StringBuilder;-><init>()V" % ri))

        method.add_insn(InsnNode("const-string v%d,\"%s(\"" % \
                                 (ri + 1, m.split('(', 1)[0])))
        append_i = InsnNode("invoke-virtual \
{v%d, v%d}, Ljava/lang/StringBuilder;->\
append(Ljava/lang/String;)Ljava/lang/StringBuilder;" % \
                            (ri, ri + 1))
        method.add_insn(append_i)
        
        # print parameters
        pi = 1
        for k in range(1, para_num):
            p = method.paras[k]
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)

            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {p%d}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             (pi, p.get_desc())))
                    pi += 1
                else:
                    method.add_insn(InsnNode("invoke-static \
{p%d, p%d}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                        (pi, pi + 1, p.get_desc())))
                    pi += 2
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {p%d}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;" % (pi, )))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

            if k < para_num - 1:
                method.add_insn(InsnNode("const-string v%d, \" | \"" % \
                                         (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("const-string v%d, \")\"" % (ri + 1)))
        method.add_insn(append_i)

        # print return value
        p = method.ret
        if p.void:
            method.add_insn(InsnNode("const-string v%d, \"%s\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
        else:
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {v1}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                else:
                    method.add_insn(InsnNode("invoke-static \
{v1, v2}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {v1}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;"))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
        method.add_insn(InsnNode("invoke-static {v%d}, \
Ldroidbox/apimonitor/Helper;->log(Ljava/lang/String;)V" % \
                                 (ri + 1, )))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("return v1"))
                else:
                    method.add_insn(InsnNode("return-wide v1"))
            else:
                method.add_insn(InsnNode("return-object v1"))
        else:
            method.add_insn(InsnNode("return-void"))

        start = LabelNode(":droidbox_try_start", 0)
        end = LabelNode(":droidbox_try_end", 1)
        index = len(method.insns)
        ret = LabelNode(":droidbox_return", index - 1)
        handler = LabelNode(":droidbox_handler", index)
        line = ".catch Ljava/lang/Exception; {:droidbox_try_start .. \
:droidbox_try_end} :droidbox_handler"
        TryNode(line, start, end, handler)
        method.add_label([start, end, ret, handler])

        method.add_insn(InsnNode("move-exception v0"))
        method.add_insn(InsnNode("invoke-virtual {v0}, \
Ljava/lang/Exception;->printStackTrace()V"))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("const/4 v1, 0x0"))
                else:
                    method.add_insn(InsnNode("const-wide/16 v1, 0x0"))
            else:
                method.add_insn(InsnNode("const/4 v1, 0x0"))
        method.add_insn(InsnNode("goto :droidbox_return"))

        method.set_registers(para_num + ri + 2)
        stub_class.add_method(method)

        i = m.find('(')
        self.method_map[m] = "L" + PKG_PREFIX + "/" + segs[0][1:] + "->" + \
                method.get_desc()


    def __add_stub_cons(self, stub_class, m):
        segs = m.rsplit("->", 1)
        desc = segs[1].replace("<init>", "droidbox_cons")
        i = desc.find(')')
        desc = desc[:i + 1] + segs[0]
        method = MethodNode()
        method.set_desc(desc)
        method.add_access(["public", "static"])

        para_num = len(method.paras)
        reg_num = method.get_paras_reg_num()
        ri = 1

        method.add_insn(InsnNode("new-instance v1, %s" % segs[0]))

        if reg_num <= 4:
            i = "invoke-direct {v1, %s}, %s" % \
                    (", ".join(["p%d" % k for k in range(reg_num)]), \
                     m)
            method.add_insn(InsnNode(i)) 
        else:
            for k in range(reg_num):
                method.add_insn(InsnNode("move-object v%d, p%d" % (k + 2, k)))
            i = "invoke-direct/range {v1 .. v%d}, %s" % \
                    (reg_num + 1, )
            method.add_insn(InsnNode(i)) 

        ri += 1

        method.add_insn(InsnNode("new-instance \
v%d, Ljava/lang/StringBuilder;" % ri))
        method.add_insn(InsnNode("invoke-direct \
{v%d}, Ljava/lang/StringBuilder;-><init>()V" % ri))

        method.add_insn(InsnNode("const-string v%d,\"%s(\"" % \
                                 (ri + 1, m.split('(', 1)[0])))
        append_i = InsnNode("invoke-virtual \
{v%d, v%d}, Ljava/lang/StringBuilder;->\
append(Ljava/lang/String;)Ljava/lang/StringBuilder;" % \
                            (ri, ri + 1))
        method.add_insn(append_i)
        
        # print parameters
        pi = 0
        for k in range(0, para_num):
            p = method.paras[k]
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)

            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {p%d}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             (pi, p.get_desc())))
                    pi += 1
                else:
                    method.add_insn(InsnNode("invoke-static \
{p%d, p%d}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                        (pi, pi + 1, p.get_desc())))
                    pi += 2
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {p%d}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;" % (pi, )))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

            if k < para_num - 1:
                method.add_insn(InsnNode("const-string v%d, \" | \"" % \
                                         (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("const-string v%d, \")\"" % (ri + 1)))
        method.add_insn(append_i)

        # print return value
        p = method.ret
        if p.void:
            method.add_insn(InsnNode("const-string v%d, \"%s\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
        else:
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {v1}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                else:
                    method.add_insn(InsnNode("invoke-static \
{v1, v2}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {v1}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;"))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
        method.add_insn(InsnNode("invoke-static {v%d}, \
Ldroidbox/apimonitor/Helper;->log(Ljava/lang/String;)V" % \
                                 (ri + 1, )))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("return v1"))
                else:
                    method.add_insn(InsnNode("return-wide v1"))
            else:
                method.add_insn(InsnNode("return-object v1"))
        else:
            method.add_insn(InsnNode("return-void"))

        start = LabelNode(":droidbox_try_start", 0)
        end = LabelNode(":droidbox_try_end", 2)
        index = len(method.insns)
        ret = LabelNode(":droidbox_return", index - 1)
        handler = LabelNode(":droidbox_handler", index)
        line = ".catch Ljava/lang/Exception; {:droidbox_try_start .. \
:droidbox_try_end} :droidbox_handler"
        TryNode(line, start, end, handler)
        method.add_label([start, end, ret, handler])

        method.add_insn(InsnNode("move-exception v0"))
        method.add_insn(InsnNode("invoke-virtual {v0}, \
Ljava/lang/Exception;->printStackTrace()V"))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("const/4 v1, 0x0"))
                else:
                    method.add_insn(InsnNode("const-wide/16 v1, 0x0"))
            else:
                method.add_insn(InsnNode("const/4 v1, 0x0"))
        method.add_insn(InsnNode("goto :droidbox_return"))

        method.set_registers(para_num + ri + 1)
        stub_class.add_method(method)

        i = m.find('(')
        self.method_map[m] = "L" + PKG_PREFIX + "/" + segs[0][1:] + "->" + \
                method.get_desc()

#invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;
    def __add_stub_static(self, stub_class, m):
        segs = m.rsplit("->", 1)

        method = MethodNode()
        method.set_desc(segs[1])
        method.add_access(["public", "static"])

        para_num = len(method.paras)
        reg_num = method.get_paras_reg_num()
        ri = 1

        if reg_num <= 5:
            i = "invoke-static {%s}, %s" % \
                    (", ".join(["p%d" % k for k in range(reg_num)]), m)
        else:
            i = "invoke-static/range {p0 .. p%d}, %s" % (opcode, reg_num - 1, m) 

        method.add_insn(InsnNode(i)) 

        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("move-result v1"))
                    ri += 1
                else:
                    method.add_insn(InsnNode("move-result-wide v1"))
                    ri += 2
            else:
                method.add_insn(InsnNode("move-result-object v1"))
                ri += 1

        method.add_insn(InsnNode("new-instance \
v%d, Ljava/lang/StringBuilder;" % ri))
        method.add_insn(InsnNode("invoke-direct \
{v%d}, Ljava/lang/StringBuilder;-><init>()V" % ri))

        method.add_insn(InsnNode("const-string v%d,\"%s(\"" % \
                                 (ri + 1, m.split('(', 1)[0])))
        append_i = InsnNode("invoke-virtual \
{v%d, v%d}, Ljava/lang/StringBuilder;->\
append(Ljava/lang/String;)Ljava/lang/StringBuilder;" % \
                            (ri, ri + 1))
        method.add_insn(append_i)
        
        # print parameters
        pi = 0
        for k in range(0, para_num):
            p = method.paras[k]
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)

            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {p%d}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             (pi, p.get_desc())))
                    pi += 1
                else:
                    method.add_insn(InsnNode("invoke-static \
{p%d, p%d}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                        (pi, pi + 1, p.get_desc())))
                    pi += 2
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {p%d}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;" % (pi, )))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

            if k < para_num - 1:
                method.add_insn(InsnNode("const-string v%d, \" | \"" % \
                                         (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("const-string v%d, \")\"" % (ri + 1)))
        method.add_insn(append_i)

        # print return value
        p = method.ret
        if p.void:
            method.add_insn(InsnNode("const-string v%d, \"%s\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
        else:
            method.add_insn(InsnNode("const-string v%d, \"%s=\"" % (ri + 1,
                                     p.get_desc())))
            method.add_insn(append_i)
            if p.basic:
                if p.words == 1:
                    method.add_insn(InsnNode("invoke-static {v1}, \
Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                else:
                    method.add_insn(InsnNode("invoke-static \
{v1, v2}, Ljava/lang/String;->valueOf(%s)Ljava/lang/String;" % \
                                             p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
            else:
                method.add_insn(InsnNode("invoke-static {v1}, \
Ldroidbox/apimonitor/Helper;->toString(Ljava/lang/Object;)Ljava/lang/String;"))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)

        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
        method.add_insn(InsnNode("invoke-static {v%d}, \
Ldroidbox/apimonitor/Helper;->log(Ljava/lang/String;)V" % \
                                 (ri + 1, )))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("return v1"))
                else:
                    method.add_insn(InsnNode("return-wide v1"))
            else:
                method.add_insn(InsnNode("return-object v1"))
        else:
            method.add_insn(InsnNode("return-void"))

        start = LabelNode(":droidbox_try_start", 0)
        end = LabelNode(":droidbox_try_end", 1)
        index = len(method.insns)
        ret = LabelNode(":droidbox_return", index - 1)
        handler = LabelNode(":droidbox_handler", index)
        line = ".catch Ljava/lang/Exception; {:droidbox_try_start .. \
:droidbox_try_end} :droidbox_handler"
        TryNode(line, start, end, handler)
        method.add_label([start, end, ret, handler])

        method.add_insn(InsnNode("move-exception v0"))
        method.add_insn(InsnNode("invoke-virtual {v0}, \
Ljava/lang/Exception;->printStackTrace()V"))
        if not method.ret.void:
            if method.ret.basic:
                if method.ret.words == 1:
                    method.add_insn(InsnNode("const/4 v1, 0x0"))
                else:
                    method.add_insn(InsnNode("const-wide/16 v1, 0x0"))
            else:
                method.add_insn(InsnNode("const/4 v1, 0x0"))
        method.add_insn(InsnNode("goto :droidbox_return"))

        method.set_registers(para_num + ri + 2)
        stub_class.add_method(method)

        i = m.find('(')
        self.method_map[m] = "L" + PKG_PREFIX + "/" + segs[0][1:] + "->" + \
                method.get_desc()



