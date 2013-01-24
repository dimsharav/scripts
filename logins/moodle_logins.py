#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: logins.py
Author: Дмитрий Шаравьев
Description:
Создание минимального набора полей для ввода пользователей в Moodle
Формат полей:
http://docs.moodle.org/22/en/Upload_users#File_formats_for_upload_users_file

Зависимости:
Python 3
pwgen

Использование:
    logins.py FILE
    FILE     - файл со списком строк
'''

import subprocess
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


def csv_create(lines):
    lines_csv = ['username,password,lastname,firstname,email']
    for str in lines:
        name = str.split()[:2]
        username = translit(name[0].lower())
        password = subprocess.getoutput('pwgen 8 1')
        email = username + '@prk.local'
        line = [username, password] + name + [email]
        lines_csv.append(','.join(line))

    return lines_csv


def main():
    parser = OptionParser(prog="logins.py",
                          usage="%prog FILE")
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        exit()

    f = open(args[0], "r")
    f_csv = open(args[0]+'.csv', "w")
    for str in csv_create(f.readlines()):
        f_csv.write(str+'\n')

    f.close()
    f_csv.close()


if __name__ == '__main__':
    main()
