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

PKG_PREFIX = "droidbox"
LOG_TAG = "DroidBox"

class JavaType(object):

    def __init__(self, smali_type):
        self.java_type = ""
        self.dim = 0
        self.basic = None

        self.__parse__(smali_type)

    def __parse__(self, smali_type):
        self.dim = smali_type.rfind('[') + 1
        smali_type = smali_type[self.dim:]

        if BASIC_TYPES.has_key(smali_type[0]):
            self.java_type = BASIC_TYPES[smali_type[0]]
            self.basic = True
        elif smali_type[0] == 'L':
            self.java_type = smali_type[1:-1].replace('/', '.')
            self.basic = False

    def get_java_desc(self):
        return self.java_type + self.dim * "[]"

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
                stub_class = StubClass(segs[0])
                self.stub_classes[segs[0]] = stub_class
                self.class_map[segs[0]] = "L" + PKG_PREFIX + "/" + segs[0][1:]
            stub_class.add(segs[1])
            i = m.find('(')
            self.method_map[m] = "L" + PKG_PREFIX + "/" + m[1:i + 1] + \
                    segs[0] + m[i + 1:]
# Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
# Ldroidbox/android/widget/TextView;->setText(Landroid/widget/TextView;Ljava/lang/CharSequence;)V"

    def get_class_descs(self):
        return self.class_map.values()

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
        self.buf.append("package %s;" % self.package.replace('/', '.'))
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
        self.ret = JavaType(self.method_short_desc[p2 + 1:])
        self.paras = []
        self.__parse_paras(self.method_short_desc[p1 + 1:p2])

    def __repr__(self):
        return self.method_short_desc

    def __parse_paras(self, paras):
        self.paras = []
        self.paras.append(JavaType(self.class_desc))
        index = 0
        dim = 0
        while index < len(paras):
            c = paras[index]
            if c == '[':
                dim += 1
                index += 1
            elif BASIC_TYPES.has_key(c):
                self.paras.append(JavaType(paras[index - dim:index + 1]))
                index += 1
                dim = 0
            else:
                tmp = paras.find(';', index)
                self.paras.append(JavaType(paras[index - dim:tmp + 1]))
                index = tmp + 1
                dim = 0

    def gen(self):
        self.buf = []
        self.buf.append("public static %s %s(%s) {" % \
                (self.ret.get_java_desc(), self.name, \
                ', '.join( \
                    ["%s p%d" % \
                        (self.paras[i].get_java_desc(), i) for i in range(len(self.paras))])))
        if self.ret.get_java_desc() != "void":
            self.buf.append("%s ret;" % self.ret.get_java_desc())
        self.buf.append("try {")
        if self.ret.get_java_desc() == "void":
            self.buf.append("p0.%s(%s);" % \
                    (self.name, \
                    ', '.join(["p%d" % i for i in range(1, len(self.paras))])))
        else:
            self.buf.append("ret = p0.%s(%s);" % \
                    (self.name, \
                    ', '.join(["p%d" % i for i in range(1, len(self.paras))])))
            self.buf.extend(self.gen_log(self.ret, "ret"))

        self.buf.append("Log.v(TAG, \"%s->%s\");" % \
                (self.class_desc, self.method_short_desc))
        for i in range(1, len(self.paras)):
            self.buf.extend(self.gen_log(self.paras[i], 'p' + str(i)))

        if self.ret.get_java_desc() != "void":
            self.buf.append("return ret;")
        self.buf.append("} catch (Exception e) {")
        self.buf.append("e.printStackTrace();")
        if self.ret.get_java_desc() != "void":
            if self.ret.basic:
                self.buf.append("return 0;")
            else:
                self.buf.append("return null;")
        self.buf.append("}")
        self.buf.append("}")

    def gen_log(self, java_type, para_name):
        buf = []
        if java_type.get_java_desc() == "void":
            return buf
        if java_type.dim == 0:
            if java_type.basic:
                buf.append("Log.v(TAG, \"%s:\"+String.valueOf(%s));" % \
                        (para_name, para_name))
            else:
                buf.append("Log.v(TAG, \"%s:\"+%s.toString());" % \
                        (para_name, para_name))
        return buf


