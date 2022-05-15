#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
import collections


Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQLA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards.insert(index, value)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self
