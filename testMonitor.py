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
from apkil import smali, monitor, logger 
from subprocess import call

EXPORT_FOLDER = "examples/java"
# print(monitor.smali2java_type('Landroid/widget/TextView;'))
m = monitor.APIMonitor([ \
        "Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V", \
        "Landroid/widget/TextView;->setNBText(Ljava/lang/CharSequence;I[[IZ)V", \
        "Landroid/test/TextView;->setNBText(Ljava/lang/CharSequence;I[[IZ)V", \
        ])
m.export(EXPORT_FOLDER)
for c in m.stub_classes.values():
    c.gen()
    print '\n'.join(c.buf)
