#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from logger import log
from smali import ClassNode, MethodNode, FieldNode, InsnNode, \
                  TypeNode, LabelNode, TryNode

PKG_PREFIX = "droidbox"
LOG_TAG = "DroidBox"

class APIMonitor(object):

    def __init__(self, method_descs):
        self.method_descs = method_descs
        self.stub_classes = {}
        self.method_map = {}
        self.class_map = {}
        for m in method_descs:
            self.add_stub_method(m)

    def __repr__(self):
        pass

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

            # .field private static final TAG:Ljava/lang/String; = "DroidBox"
            # f = FieldNode()
            # f.set_desc("Ljava/lang/String;")
            # f.add_access(["private", "static", "final"])
            # f.set_name("TAG")
            # f.set_value('"' + LOG_TAG + '"')
            # stub_class.add_field(f)

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
        ri = 1

        if para_num <= 5:
            i = "invoke-virtual {%s}, %s" % \
                    (", ".join(["p%d" % k for k in range(para_num)]), m)
        else:
            i = "invoke-virtual/range {p0 .. p%d}, %s" % (opcode, para_num - 1, m) 

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
        conds = []
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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz p%d, :droidbox_cond_%d" %\
                                         (pi, cond_tag)))
                method.add_insn(InsnNode("invoke-virtual {p%d}, \
%s->toString()Ljava/lang/String;" % (pi, p.get_desc())))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz v1, :droidbox_cond_%d" %\
                                         cond_tag))
                method.add_insn(InsnNode("invoke-virtual {v1}, \
%s->toString()Ljava/lang/String;" % p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

        method.add_insn(InsnNode("const-string v%d, \"DroidBox\"" % \
                (ri + 1)))
        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 2)))
        method.add_insn(InsnNode("invoke-static {v%d, v%d}, \
Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I" % \
                                 (ri + 1, ri + 2)))
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

        for t in conds:
            index = len(method.insns)
            cond = LabelNode(":droidbox_cond_%d" % t, index)
            method.add_label(cond)
            method.add_insn(InsnNode("const-string v%d, \"null\"" %\
                                     (ri + 1)))
            method.add_insn(append_i)
            method.add_insn(InsnNode("goto :droidbox_goto_%d" % t))

        method.set_registers(para_num + ri + 3)
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
        ri = 1

        method.add_insn(InsnNode("new-instance v1, %s" % segs[0]))
        if para_num <= 4:
            i = "invoke-direct {v1, %s}, %s" % \
                    (", ".join(["p%d" % k for k in range(para_num)]), \
                     m)
        else:
            print "constructor with more than 4 paras!"
            sys.exit(1)

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
        conds = []
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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz p%d, :droidbox_cond_%d" %\
                                         (pi, cond_tag)))
                method.add_insn(InsnNode("invoke-virtual {p%d}, \
%s->toString()Ljava/lang/String;" % (pi, p.get_desc())))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz v1, :droidbox_cond_%d" %\
                                         cond_tag))
                method.add_insn(InsnNode("invoke-virtual {v1}, \
%s->toString()Ljava/lang/String;" % p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

        method.add_insn(InsnNode("const-string v%d, \"DroidBox\"" % \
                (ri + 1)))
        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 2)))
        method.add_insn(InsnNode("invoke-static {v%d, v%d}, \
Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I" % \
                                 (ri + 1, ri + 2)))
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

        for t in conds:
            index = len(method.insns)
            cond = LabelNode(":droidbox_cond_%d" % t, index)
            method.add_label(cond)
            method.add_insn(InsnNode("const-string v%d, \"null\"" %\
                                     (ri + 1)))
            method.add_insn(append_i)
            method.add_insn(InsnNode("goto :droidbox_goto_%d" % t))

        method.set_registers(para_num + ri + 2)
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
        ri = 1

        if para_num <= 5:
            i = "invoke-static {%s}, %s" % \
                    (", ".join(["p%d" % k for k in range(para_num)]), m)
        else:
            i = "invoke-static/range {p0 .. p%d}, %s" % (opcode, para_num - 1, m) 

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
        conds = []
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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz p%d, :droidbox_cond_%d" %\
                                         (pi, cond_tag)))
                method.add_insn(InsnNode("invoke-virtual {p%d}, \
%s->toString()Ljava/lang/String;" % (pi, p.get_desc())))
                pi += 1
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

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
                cond_tag = len(method.insns)
                conds.append(cond_tag)
                method.add_insn(InsnNode("if-eqz v1, :droidbox_cond_%d" %\
                                         cond_tag))
                method.add_insn(InsnNode("invoke-virtual {v1}, \
%s->toString()Ljava/lang/String;" % p.get_desc()))
                method.add_insn(InsnNode("move-result-object v%d" % (ri + 1)))
                method.add_insn(append_i)
                index = len(method.insns)
                cond = LabelNode(":droidbox_goto_%d" % cond_tag, index)
                method.add_label(cond)

        method.add_insn(InsnNode("const-string v%d, \"DroidBox\"" % \
                (ri + 1)))
        method.add_insn(InsnNode("invoke-virtual {v%d}, \
Ljava/lang/StringBuilder;->toString()Ljava/lang/String;" % ri))
        method.add_insn(InsnNode("move-result-object v%d" % (ri + 2)))
        method.add_insn(InsnNode("invoke-static {v%d, v%d}, \
Landroid/util/Log;->v(Ljava/lang/String;Ljava/lang/String;)I" % \
                                 (ri + 1, ri + 2)))
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

        for t in conds:
            index = len(method.insns)
            cond = LabelNode(":droidbox_cond_%d" % t, index)
            method.add_label(cond)
            method.add_insn(InsnNode("const-string v%d, \"null\"" %\
                                     (ri + 1)))
            method.add_insn(append_i)
            method.add_insn(InsnNode("goto :droidbox_goto_%d" % t))

        method.set_registers(para_num + ri + 3)
        stub_class.add_method(method)

        i = m.find('(')
        self.method_map[m] = "L" + PKG_PREFIX + "/" + segs[0][1:] + "->" + \
                method.get_desc()

