#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
import sys
import time
import shutil
import os
from androguard.core.bytecodes import apk
from apkil import smali, monitor, logger 
from subprocess import call

APK = "examples/DroidBoxTests.apk"
DEX = "examples/DroidBoxTests.dex"
SMALI_DIR = "examples/DroidBoxTests_smali"

a = apk.APK(APK)
dex_file = open(DEX, 'w')
dex_file.write(a.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', SMALI_DIR, DEX])
s = smali.SmaliTree(SMALI_DIR)

NEW_OUT = "examples/new"
NEW_DEX = "examples/classes.dex"
NEW_APK = "examples/new.apk"

# sys.exit(0)

API_LIST = [ "Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V", \
        "Ljava/io/OutputStreamWriter;->write(Ljava/lang/String;)V"
        ]

TEMPLATE = "template/APIMonitor"
EXPORT_FOLDER = "examples/APIMonitor/java"

if os.path.exists(EXPORT_FOLDER):
    shutil.rmtree(EXPORT_FOLDER)
shutil.copytree(TEMPLATE, EXPORT_FOLDER)
m = monitor.APIMonitor(API_LIST)
m.export(os.path.join(EXPORT_FOLDER, "src"))
call(args=["android", "update", "project", "--path", EXPORT_FOLDER])
call(args=["ant", "debug", "-buildfile", \
    os.path.join(EXPORT_FOLDER, "build.xml")])

# sys.exit(0)

dex_file_path = os.path.join(EXPORT_FOLDER, "bin", "classes.dex")
MONITOR_SMALI = "examples/APIMonitor/smali"

call(args=['baksmali', '-b', '-o', MONITOR_SMALI, dex_file_path])
m_s = smali.SmaliTree(MONITOR_SMALI)

# print repr(m.method_map)

for api in API_LIST:
    insns = s.get_insn35c("invoke-virtual", api)
    for i in insns:
        i.obj.replace("invoke-static", m.method_map[api])

for c in m.get_class_descs():
    print c
    s.add_class(m_s.get_class(c))
s.save(NEW_OUT)
call(args=['smali', '-a', '6', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/androguard", "androguard", "haimen!!" )

