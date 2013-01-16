#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from androguard.core.bytecodes import apk
from apkil import smali, monitor, logger
from apkil.api_permissions import API_BY_PERMISSION
from subprocess import call


APK = "examples/APKILTests.apk"
DEX = "examples/APKILTests.dex"
SMALI_DIR = "examples/APKILTests"
APK = "examples/LeCha_v1.09.apk"
DEX = "examples/LeCha_v1.09.dex"
SMALI_DIR = "examples/LeCha_v1.09"

NEW_OUT = "examples/new"
NEW_DEX = "examples/classes.dex"
NEW_APK = "examples/new.apk"

a = apk.APK(APK)
dex_file = open(DEX, 'w')
dex_file.write(a.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', SMALI_DIR, DEX])
s = smali.SmaliTree(SMALI_DIR)

api_list = []
perms = a.get_permissions()
for p in perms:
    print p
    if API_BY_PERMISSION.has_key(p):
        for ml in API_BY_PERMISSION[p].values():
            api_list.extend(ml)

mo = monitor.APIMonitor(api_list)
s = mo.inject(s)
s.save(NEW_OUT)

call(args=['smali', '-a', '7', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/apkil", "apkil", "apkilapkil" )

