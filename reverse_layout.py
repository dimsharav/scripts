#!/usr/bin/env python
'''
Исправление ошибки раскладки
'''

letters_in = ("`qwertyuiop[]asdfghjkl;'zxcvbnm,./~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?@#$^&")
letters_out = ("ёйцукенгшщзхъфывапролджэячсмитьбю.ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,\"№;:?")

str_in = input('Введите строку на английской раскладке: ')
str_out = ''

for letter in str_in:
    if letter in letters_in:
        i = letters_in.find(letter)
        str_out += letters_out[i]
    else:
        str_out += letter

print(str_out)
