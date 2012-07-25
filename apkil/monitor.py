#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from logger import log
from smali import ClassNode, MethodNode, FieldNode, InsnNode, TypeNode

# Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
# Lorg/honeynet/apimonitor/APIMonitor;->android_widget_TextView__setText(Landroid/widget/TextView;Ljava/lang/CharSequence;)V
# example java code:
# package org.honeynet.apimonitor;
# import android.util.Log;
# import android.widget.TextView;

# public class APIMonitor {
#	 private static final String TAG = "APIMonitor";
#	 public static void android_widget_TextView__setText(TextView textView, CharSequence text) {
#  		 textView.setText(text);
# 		 Log.v(TAG, text.toString());
# 	 }
# }

PKG_PREFIX = "droidbox"
LOG_TAG = "DroidBox"

class APIMonitor(object):

    def __init__(self, method_descs):
        self.method_descs = method_descs
        self.stub_classes = {}
        self.method_map = {}
        self.class_map = {}
        for m in method_descs:
            segs = m.rsplit("->", 1)
            if self.stub_classes.has_key(segs[0]):
                stub_class = self.stub_classes[segs[0]]
            else:
                stub_class = ClassNode()
                stub_class.set_name("L" + PKG_PREFIX + "/" + segs[0][1:])
                stub_class.set_super_name("Ljava/lang/Object;")

                # .field private static final TAG:Ljava/lang/String; = "DroidBox"
                f = FieldNode()
                f.set_desc("Ljava/lang/String;")
                f.add_access(["private", "static", "final"])
                f.set_name("TAG")
                f.set_value('"' + LOG_TAG + '"')
                stub_class.add_field(f)

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

            # stub_class.add(segs[1])
            # invoke-virtual {p0, p1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
            method = MethodNode()
            method.set_desc(segs[1])
            method.add_access(["public", "static"])
            method.add_para(TypeNode(segs[0]))
            method.set_registers(2)
            i1 = InsnNode("invoke-virtual {p0, p1}, \
                    Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V")
            i2 = InsnNode("return-void")
            method.add_insn([i1, i2])
            stub_class.add_method(method)

            i = m.find('(')
            self.method_map[m] = "L" + PKG_PREFIX + "/" + m[1:i + 1] + \
                    segs[0] + m[i + 1:]
# Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
# Ldroidbox/android/widget/TextView;->setText(Landroid/widget/TextView;Ljava/lang/CharSequence;)V"

    def __repr__(self):
        pass

