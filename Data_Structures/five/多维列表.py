#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
if __name__ == "__main__":
    # 正确的多维列表
    data = [[0] * 3 for i in range(6)]
    print(data)
    data[0][1] = 3
    print(data)  # 二级列表指向不是同一个地址
