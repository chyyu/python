#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
"""
实现
v1 = Vector2d(3, 4)
print(v1.x, v1.y)
# >>> 3.0 4.0

x, y = v1
x, y
# >>> (3.0, 4.0)

v1
# >>> Vector2d(3.0, 4.0)

v1_clone = eval(repr(v1))
v1 == v1_clone
# >>> True

print(v1)
# >>> (3.0, 4.0)

v1 = Vector2d(3, 4)
print(format(v1, '.3f'))
"""
from array import array
import math


class Vector2d:
    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # Not very clear
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec=""):
        components = (format(c, format_spec) for c in self)
        return "({}, {})".format(*components)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


v1 = Vector2d(3, 4)
print(hash(v1))
