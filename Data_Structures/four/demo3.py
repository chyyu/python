#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy


# 对于一个含有n个元素的序列S，描述一个递归算法查找其最大值。所给出的递归算法时间复杂度和空间复杂度各是多少？
def search_max(S):
    return search_max1(S, len(S)-1)


def search_max1(S, index):
    if index == 0:
        return S[index]
    else:
        m = search_max1(S, index-1)
        return S[index] if S[index] > m else m


print(search_max([1, 2, 3, 4, 5, 6, 0, 8, 9, 1]))
