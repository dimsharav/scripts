#!/usr/bin/env python
'''
Исправление ошибки раскладки
'''

letters_eng = ("`qwertyuiop[]asdfghjkl;'zxcvbnm,./~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?@#$^&")
letters_rus = ("ёйцукенгшщзхъфывапролджэячсмитьбю.ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,\"№;:?")
letters = dict(zip(letters_eng, letters_rus))

str_in = input('Введите строку на английской раскладке: ')
str_out = ''

for letter in str_in:
    if letter in letters_eng:
        str_out += letters[letter]
    else:
        str_out += letter

print(str_out)
