#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from androguard.core.bytecodes import apk
from apkil import smali, monitor, logger 
from subprocess import call

MONITOR_CLASS = "Lorg/honeynet/apimonitor/APIMonitor;"

M_APK = "examples/APIMonitor.apk"
M_DEX = "examples/APIMonitor.dex"
M_SMALI = "examples/APIMonitor"

APK = "examples/APKILTests.apk"
DEX = "examples/APKILTests.dex"
SMALI_DIR = "examples/APKILTests"

#APK = "examples/HelloChinese.apk"
#DEX = "examples/HelloChinese.dex"
#SMALI_DIR = "examples/HelloChinese"

NEW_OUT = "examples/new"
NEW_DEX = "examples/classes.dex"
NEW_APK = "examples/new.apk"

a = apk.APK(APK)
dex_file = open(DEX, 'w')
dex_file.write(a.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', SMALI_DIR, DEX])
s = smali.SmaliTree(SMALI_DIR)
# print repr(s)
# sys.exit(0)

#API_LIST = [ "Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V"]
API_LIST = [ #"Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V", \
#"Landroid/content/ContentValues;->put(Ljava/lang/String;Ljava/lang/Integer;)V", \
#"Landroid/content/ContentValues;->put(Ljava/lang/String;Ljava/lang/String;)V", \
"static:Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;", \
"constructor:Landroid/content/Intent;-><init>(Ljava/lang/String;)V", \
"instance:Lapkil/tests/APKIL;->openFileOutput(Ljava/lang/String;I)Ljava/io/FileOutputStream;", \
"instance:Ljava/io/OutputStreamWriter;->write(Ljava/lang/String;)V", \
"instance:Lapkil/tests/APKIL;->openFileInput(Ljava/lang/String;)Ljava/io/FileInputStream;",
"instance:Ljava/io/BufferedReader;->readLine()Ljava/lang/String;", \
]
mo = monitor.APIMonitor(API_LIST)

for api in API_LIST:
    segs = api.split(':', 1)
    method_type = segs[0]
    api = segs[1]
    segs = api.split("->")
    if method_type == "constructor":
        for c in s.classes:
            for m in c.methods:
                for i in range(len(m.insns)):
                    insn = m.insns[i]
                    if insn.fmt == "35c" and \
                       insn.opcode_name == "invoke-direct" and \
                       insn.obj.method_desc == api :
                        insn.obj.replace("invoke-static", mo.method_map[api])
                        r = insn.obj.registers.pop(0)
                        m.insert_insn(smali.InsnNode(\
"move-result-object %s" % r), i + 1, 0)
            
    elif method_type == "instance":
        for c in s.classes:
            for m in c.methods:
                for i in range(len(m.insns)):
                    insn = m.insns[i]
                    if insn.fmt == "35c" and \
                       insn.opcode_name == "invoke-virtual" and \
                       insn.obj.method_desc == api :
                        insn.obj.replace("invoke-static", mo.method_map[api])
    elif method_type == "static":
        for c in s.classes:
            for m in c.methods:
                for i in range(len(m.insns)):
                    insn = m.insns[i]
                    if insn.fmt == "35c" and \
                       insn.opcode_name == "invoke-static" and \
                       insn.obj.method_desc == api :
                        insn.obj.replace("invoke-static", mo.method_map[api])

for c in mo.stub_classes.values():
    s.add_class(c)
    
s.save(NEW_OUT)
#sys.exit(0)

call(args=['smali', '-a', '7', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/apkil", "apkil", "apkilapkil" )

