#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher"""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation"""
        encoder = list([None] * 26)
        decoder = list([None] * 26)
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """Return string representing encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret"""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string"""
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():
                j = ord(msg[i]) - ord('A')
                msg[i] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    msg = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(msg)
    print('secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)
