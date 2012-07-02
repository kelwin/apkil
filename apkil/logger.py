#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

debug = 'TERM'
log = None

def Pass(*args):
    pass

if debug == "TERM":
	logging.basicConfig(level=logging.DEBUG,
            format='%(filename)s Line:%(lineno)d Fun:%(funcName)s  %(message)s',)
	log = logging.debug
elif debug == "FILE":
	logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s Line:%(lineno)d Fun:%(funcName)s  %(message)s',
            filename='./apkil.log',
            filemode='w')
	log = logging.debug
else:
	log = Pass

