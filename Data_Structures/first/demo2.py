#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        假设有足够的信用额度，向卡收取给定的价格。

        如果已处理费用，则返回True；如果指控被否认，则为假。
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount


cc = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5409", 1000)


