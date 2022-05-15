#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
# 二路递归
# 计算一个列表元素和

def binary_sum(L, start, stop):
    """Calculate the sum of elements"""

    if start > stop:
        return 0
    elif start == stop - 1:
        return L[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(L, start, mid) + binary_sum(L, mid, stop)


print(binary_sum([1, 2, 3, 4, 5, 6], 0, 3))
