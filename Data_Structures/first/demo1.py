#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy

# data = [1, 2, 3]
# i = iter(data)
# next(i)
def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        future = a + b
        a = b
        b = future


x = fibonacci()
if __name__ == '__main__':
    print(next(x))
