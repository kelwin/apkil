#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from androguard.core.bytecodes import apk
from apkil import smali, logger 
from subprocess import call

def method_to_monitor(method_desc):
# Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
# Lorg/honeynet/apimonitor/APIMonitor;->android_widget_TextView__setText(Landroid/widget/TextView;Ljava/lang/CharSequence;)V
    class_name = "org/honeynet/apimonitor/APIMonitor;"
    return ""

MONITOR_CLASS = "Lorg/honeynet/apimonitor/APIMonitor;"

M_APK = "examples/APIMonitor.apk"
M_DEX = "examples/APIMonitor.dex"
M_SMALI = "examples/APIMonitor"

APK = "examples/HelloChinese.apk"
DEX = "examples/HelloChinese.dex"
SMALI_DIR = "examples/HelloChinese"

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

m_a = apk.APK(M_APK)
dex_file = open(M_DEX, 'w')
dex_file.write(m_a.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', M_SMALI, M_DEX])
m_s = smali.SmaliTree(M_SMALI)
# print repr(s)

insns = s.get_insn35c("invoke-virtual","Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V")
new_opcode_name = "invoke-static"
new_method_desc = "Lorg/honeynet/apimonitor/APIMonitor;->android_widget_TextView__setText(Landroid/widget/TextView;Ljava/lang/CharSequence;)V"
for i in insns:
    i.obj.replace(new_opcode_name, new_method_desc)

s.add_class(m_s.get_class("Lorg/honeynet/apimonitor/APIMonitor;"))
s.save(NEW_OUT)
call(args=['smali', '-a', '6', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/androguard", "androguard", "haimen!!" )

