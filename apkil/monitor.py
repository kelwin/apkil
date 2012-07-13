#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from logger import log

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


CLASS_NAME = "org/honeynet/apimonitor/APIMonitor"
PKG_PREFIX = "droidbox"
LOG_TAG = "DroidBox"

def smali2java_type(t):
    if BASIC_TYPES.has_key(t[0]):
        return BASIC_TYPES[t[0]]
    elif t[0] == 'L':
        return t[1:-1].replace('/', '.')
    elif t[0] == '[':
        d = t.count('[')
        return smali2java_type(t[d:]) + d * "[]"
    else:
        return ""

class APIMonitor(object):

    def __init__(self, method_descs):
        self.method_descs = method_descs
        self.stub_classes = {}
        for m in method_descs:
            segs = m.rsplit("->", 1)
            if self.stub_classes.has_key(segs[0]):
                stub_class = self.stub_classes[segs[0]]
            else:
                stub_class = StubClass(segs[0])
                self.stub_classes[segs[0]] = stub_class
            stub_class.add(segs[1])

    def __repr__(self):
        return "%s" % \
        (''.join([repr(c) for c in self.stub_classes.values()]), )

    def export(self, foldername):
        for c in self.stub_classes.values():
            c.export(foldername)

class StubClass(object):

    def __init__(self, class_desc):
        self.buf = [] 
        segs = class_desc.rsplit('/', 1)
        self.class_name = segs[1][:-1]
        self.class_desc = class_desc
        self.package = PKG_PREFIX + '/' + segs[0][1:] 
        self.stub_methods = []

    def __repr__(self):
        return "%s\n%s\n" % (self.class_desc, self.buf)

    def add(self, method_short_desc):
        self.stub_methods.append(StubMethod(self.class_desc, method_short_desc))

    def gen(self):
        self.buf = []
        self.buf.append("package %s;" % self.package)
        self.buf.append("import android.util.Log;")
        # self.buf.append("import %s;" % self.class_desc[1:-1])
        self.buf.append("public class %s {" % self.class_name)
        self.buf.append("private static final String TAG = \"%s\";" % LOG_TAG)
        for m in self.stub_methods:
            m.gen()
            self.buf.extend(m.buf)
        self.buf.append("}")

    def export(self, foldername):
        path = os.path.join(foldername, self.package)
        if not os.path.exists(path):
            os.makedirs(path)
        filename = os.path.join(path, self.class_name + ".java")
        f = open(filename, 'w')
        self.gen()
        f.write('\n'.join(self.buf))
        f.close()

#setText(Ljava/lang/CharSequence;)V
class StubMethod(object):

    def __init__(self, class_desc, method_short_desc):
        self.buf = []
        self.class_desc = class_desc
        self.method_short_desc = method_short_desc
        p1 = self.method_short_desc.find('(')
        p2 = self.method_short_desc.find(')')
        self.name = self.method_short_desc[:p1] 
        self.ret = smali2java_type(self.method_short_desc[p2 + 1:])
        self.paras = []
        self.__parse_paras(self.method_short_desc[p1 + 1:p2])

    def __repr__(self):
        return self.method_short_desc

    def __parse_paras(self, paras):
        self.paras = []
        self.paras.append(smali2java_type(self.class_desc))
        index = 0
        dim = 0
        while index < len(paras):
            c = paras[index]
            if c == '[':
                dim += 1
                index += 1
            elif BASIC_TYPES.has_key(c):
                self.paras.append(smali2java_type(paras[index - dim:index + 1]))
                index += 1
                dim = 0
            else:
                tmp = paras.find(';', index)
                self.paras.append(smali2java_type(paras[index - dim:tmp + 1]))
                index = tmp + 1
                dim = 0

    def gen(self):
        self.buf = []
        self.buf.append("public static %s %s(%s) {" % \
                (self.ret, self.name, \
                ', '.join( \
                    ["%s p%d" % \
                        (self.paras[i], i) for i in range(len(self.paras))])))
        self.buf.append("p0.%s(%s);" % (self.name, ', '.join(["p%d" % i for i in
            range(1, len(self.paras))])))
        self.buf.append("}")

