#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
# Pages165
import time


def clock(func):

    def clocked(*args):
        t0 = time.perf_counter()
