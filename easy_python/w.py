#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import re


print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '192.168.1.1'))

x = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.148.1.1')

p = re.compile("[A-Z]")

print(p.search("I love FishC,com!"))


x.group()
