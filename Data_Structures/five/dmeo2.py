#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class Scoreboard:

    def __init__(self, capacity=10):
        self._board = [None] * capacity  # reserve space for future scores
        self._n = 0  # number of actual entries

    def __getitem__(self, item):
        """Return entry at index item"""
        return self._board[item]

    def __str__(self):
        """Return string representation of high score list."""
        return '\n'.join(str(self._board[i]) for i in range(self._n))


