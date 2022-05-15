#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
x = []


def e(func):
    print(func)
    x.append(func)
    return func


@e
def f1():
    print(1)


@e
def f2():
    print(2)


def f3():
    print(3)


def main():
    print('main')
    print(x)

    f1()
    f2()
    f3()


main()
