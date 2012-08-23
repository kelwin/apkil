#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from apkil import api
import cPickle

level = 7
class_ = "android.content.ContextWrapper"
method = "<init>"

jar_name = "android-%d.jar" % level
jar_path = os.path.join("androidlib", jar_name)
data_path = os.path.join("androidlib", "android-%d.db" % level)
android_api = api.AndroidAPI()
android_api.load(data_path)

#android_api.show_classes()
for c in android_api.classes.values():
    if not c.name == "android.content.ContextWrapper":
        continue
    for m in c.methods.values():
        if m.name == method:
            print m.sdesc
        
