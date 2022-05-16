#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
def fact(n):
    """阶乘"""
    if n == 1:
        return 1
    return fact(n-1) * n


def fact_1(n, a=1):
    """阶乘"""
    if n == 1:
        return a
    a = a * n
    return fact_1(n-1, a)


if __name__ == "__main__":
    print(fact_1(4))
