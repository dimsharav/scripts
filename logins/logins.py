#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: logins.py
Author: Dmitriy Sharavyov
Description: Создание логинов из фамилий с транлитерацией
Версия Python: 3

Использование:
    logins.py FILE
    FILE     - файл со списком строк
'''

from optparse import OptionParser


def translit(s):
    """translit string 's' from russian to english"""
    dic = {'а': 'a',
           'б': 'b',
           'в': 'v',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ё': 'yo',
           'ж': 'zh',
           'з': 'z',
           'и': 'i',
           'й': 'i',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'h',
           'ц': 'c',
           'ч': 'ch',
           'ш': 'sh',
           'щ': 'sch',
           'ъ': '_',
           'ы': 'y',
           'ь': '_',
           'э': 'e',
           'ю': 'yu',
           'я': 'ya',
           '\n': ''}
    for c in dic:
        s = s.replace(c, dic[c])
    return s


def main():
    parser = OptionParser(prog="logins.py",
                          usage="%prog FILE")
    (options, args) = parser.parse_args()
    if len(args) == 1:
        f = open(args[0], "r")
    else:
        parser.print_help()
        exit()
    lines = f.readlines()
    for str in lines:
        print(translit(str.lower()))
    return None

if __name__ == '__main__':
    main()
