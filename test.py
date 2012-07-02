#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from androguard.core.bytecodes import apk
from apkil import smali, logger 
from subprocess import Popen

class Test(object):
    NAME = 1
    def __init__(self, data):
        Test.NAME += 2;
        self.data = data

debug = "TERM"
TEST = "examples/HelloChinese.apk"
OUTDIR = "examples/HelloChinese"
NEW_OUT = "examples/new"
NEW_DEX = "examples/classes.dex"
NEW_APK = "examples/new.apk"

a = apk.APK(TEST)
#dex_file = open("examples/HelloChinese.dex", 'w')
#dex_file.write(a.get_dex())
#Popen(args=['baksmali', '-b', '-o', OUTDIR, 'examples/HelloChinese.dex'])
#time.sleep(5)
s = smali.SmaliTree(OUTDIR)
print repr(s)
s.save(NEW_OUT)
Popen(args=['smali', '-o', NEW_DEX, NEW_OUT])

new_dex = open(NEW_DEX).read();
a.new_zip(filename=NEW_APK,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk( NEW_APK, \
"/Users/kelwin/Dropbox/Backup/androguard", "androguard", "haimen!!" )

