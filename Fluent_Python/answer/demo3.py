#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
def quicksort(array):
    # 创建一个排序函数
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]

        greater = [y for y in array[1:] if y > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# 测试
print(quicksort([2,3,4,61,1]))