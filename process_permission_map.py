#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from apkil.smali import TypeNode

def java_method_to_smali(method):
    i = method.find('(')
    desc = method[:i]
    j = desc.rfind('.')
    class_ = TypeNode() 
    class_.load_java(desc[:j])
    class_desc = class_.get_desc() 

    method_desc = class_desc + "->" + desc[j + 1:] + "("
    paras = method[i + 1:-1].split(',')
    for para in paras:
        t = TypeNode()
        t.load_java(para)
        method_desc += t.get_desc()
    method_desc += ')'
    return (class_desc, method_desc)

PERMISSION_MAP_FILE = "permissionmap/APICalls.txt"
PERMISSION_MAP_OUTPUT = "apkil/api_permissions.py"
pm = open(PERMISSION_MAP_FILE, 'r')

api_by_perms = {}
line = pm.readline()
line = pm.readline()
while line:
    if line.isspace():
        continue

    segs = line.split(None, 2)
    method = segs[0]
    perm = segs[1]
    class_desc, method_desc = java_method_to_smali(method)
    #print perm, class_desc, method_desc
    if not api_by_perms.has_key(perm):
        api_by_perms[perm] = {} 
    perm_dict = api_by_perms[perm]

    if not perm_dict.has_key(class_desc):
        perm_dict[class_desc] = []
    method_list = perm_dict[class_desc]
    method_list.append(method_desc)

    line = pm.readline()

pm.close()


f = open(PERMISSION_MAP_OUTPUT, 'w')
f.write("API_BY_PERMISSION = {\n")
for perm in api_by_perms.keys():
    perm_dict = api_by_perms[perm]
    f.write("\"%s\": {\n" % perm)
    for class_desc in perm_dict.keys():
        method_list = perm_dict[class_desc]
        f.write("    \"%s\": [\n" % class_desc)
        for method in method_list:
            f.write("        \"%s\",\n" % method)
        f.write("    ],\n")
    f.write("},\n")
f.write("}\n")



