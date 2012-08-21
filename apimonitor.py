#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012, The Honeynet Project. All rights reserved.
# Author: Kun Yang <kelwya@gmail.com>
#
# APKIL is free software: you can redistribute it and/or modify it under 
# the terms of version 3 of the GNU Lesser General Public License as 
# published by the Free Software Foundation.
#
# APKIL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for 
# more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with APKIL.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import shutil
import time
import argparse
from androguard.core.bytecodes import apk
from apkil import smali, monitor, logger 
from subprocess import call

parser = argparse.ArgumentParser(description=\
'Repackage apk to monitor arbitrary APIs.')
parser.add_argument('-o, --output', metavar='dirpath', type=str, nargs=1,
                    help='output directory', 
                    dest='output')
parser.add_argument('-a, --api', metavar='apilist', type=str,
                    default="config/default_api_collection",
                    help='config file of API list',
                    dest='api')
parser.add_argument('-v, --version', action='version',
                    version='DroidBoxAPIMonitor v0.1')
parser.add_argument('filename', type=str, 
                    help='path of APK file')

args = parser.parse_args()
apk_name = os.path.basename(args.filename)
root_name, ext = os.path.splitext(apk_name)
if ext != ".apk":
    print "error: not an APK file"
    sys.exit(2)

a = apk.APK(args.filename)

if args.output:
    outdir = args.output
else:
    outdir = os.path.dirname(args.filename)

api_config = args.api
mo = monitor.APIMonitor(config=api_config)

new_apk = os.path.join(outdir, root_name + "_new.apk")
outdir = os.path.join(outdir, "apimonitor_out")

if os.path.exists(outdir):
    shutil.rmtree(outdir)
os.makedirs(outdir)

dexpath = os.path.join(outdir, "origin.dex")
smalidir = os.path.join(outdir, "origin_smali") 
new_dexpath = os.path.join(outdir, "new.dex")
new_smalidir = os.path.join(outdir, "new_smali")

min_version = int(a.get_min_sdk_version())
if a.get_target_sdk_version():
    target_version = int(a.get_target_sdk_version())
else:
    target_version = min_version
level = min_version

dex_file = open(dexpath, 'w')
dex_file.write(a.get_dex())
dex_file.close()

call(args=['baksmali', '-b', '-o', smalidir, dexpath])
s = smali.SmaliTree(level, smalidir)

s = mo.inject(s, level)
s.save(new_smalidir)

call(args=['smali', '-a', str(level),
     '-o', new_dexpath, new_smalidir])

new_dex = open(new_dexpath).read();
a.new_zip(filename=new_apk,
            deleted_files="(META-INF/.)", new_files = {
            "classes.dex" : new_dex } )
apk.sign_apk(new_apk, \
"config/apkil.cert", "apkil", "apkilapkil" )

