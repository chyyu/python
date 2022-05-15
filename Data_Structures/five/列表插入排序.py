#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class CaesarCipher:
    '''Class for doing encryption(加密) and decryption(解密) using a Caesar cipher'''
    def __init__(self,shift):
        '''Construcr Caesar cipher given integar shift for ratation'''
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k+shift)%26 + ord('A'))
            decoder[k] = chr((k-shift)%26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backwad = ''.join(decoder)
    def encrypt(self,message):
        '''Return string representing encrypted message'''
        return self._transform(message,self._forward)
    def decrypt(self,secret):
        '''return decrypted message given encrypted secret'''
        return self._transform(secret,self._backwad)
    def _transform(self,original,code):
        '''Utility to perform transformation based on given code string'''
        msg = list(original.upper())
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j]
        return ''.join(msg)
def main():
    cipher = CaesarCipher(3)
    message = 'i love you'
    code = cipher.encrypt(message)
    print('the secret message is: ',code)
    answer = cipher.decrypt(code)
    print('the real meassage is: ',answer)

if __name__ == '__main__':
    main()

