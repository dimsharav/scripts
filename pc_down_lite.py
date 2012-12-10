#!/usr/bin/env python
# -*- coding: utf-8 -*-

desc = """Выключение удаленных ПК под управлением Windows.
Зависимости: Python3, Samba, pc_down.py

По-умолчанию скрипт ищет конфиг-файл ~/.pc_down_lite.conf"""

from pc_down import shutdown

from optparse import OptionParser
from subprocess import call

import configparser, getpass, os


def read_config(file=os.path.expanduser('~/.pc_down_lite.conf')):
    Config = configparser.ConfigParser()
    Config.read(file)
    username = Config.get("DEFAULT","username")
    password = Config.get("DEFAULT","password")
    return username, password


def main():
    parser = OptionParser(description=desc,
                          prog="pc_down_lite.py",
                          version="%prog \nVersion 0.1a",
                          usage="%prog PC_FOR_SHUTDOWN",
                          )
    (options, args) = parser.parse_args()
    username, password = read_config()
    if len(args) == 1:
        if args[0] == '237':
            for i in range(101, 121):
                shutdown("192.168.0.%s" % i, username, password)
        elif args[0] == '239':
            for i in range(121, 139):
                shutdown("192.168.0.%s" % i, username, password)
        else:
            shutdown(args[0], username, password)
    else:
        parser.print_help()
    return None


if __name__ == '__main__':
    main()
