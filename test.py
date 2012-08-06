#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from androguard.core.bytecodes import apk
from apkil import smali, monitor, logger 
from subprocess import call

HELPER_APK = "examples/APIMonitor.apk"
HELPER_DEX = "examples/APIMonitor.dex"
HELPER_SMALI = "examples/APIMonitor"
HELPER_CLASS = "Ldroidbox/apimonitor/Helper;"

APK = "examples/APKILTests.apk"
DEX = "examples/APKILTests.dex"
SMALI_DIR = "examples/APKILTests"

#APK = "examples/HelloChinese.apk"
#DEX = "examples/HelloChinese.dex"
#SMALI_DIR = "examples/HelloChinese"

NEW_OUT = "examples/new"
NEW_DEX = "examples/classes.dex"
NEW_APK = "examples/new.apk"

helper = apk.APK(HELPER_APK)
dex_file = open(HELPER_DEX, 'w')
dex_file.write(helper.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', HELPER_SMALI, HELPER_DEX])
helper = smali.SmaliTree(HELPER_SMALI)

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
#"instance:Ljava/io/BufferedReader;->readLine()Ljava/lang/String;", \
]
mo = monitor.APIMonitor(API_LIST)
s.add_class(helper.get_class(HELPER_CLASS))
mo.repackage(s)
s.save(NEW_OUT)
#sys.exit(0)

call(args=['smali', '-a', '7', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/apkil", "apkil", "apkilapkil" )

