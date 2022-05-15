#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import argparse, socket
from datetime import datetime


MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


