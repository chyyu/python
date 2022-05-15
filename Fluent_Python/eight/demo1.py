#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
x = [1, 2, 3]
print(id(x))

y = x
print(id(y))

x.append(2)
print(id(y))

# The id is the same
