#!/usr/bin/env python
# -*- coding: utf-8 -*-

desc = """Выключение удаленных ПК под управлением Windows.
Зависимости: Python3, Samba (для net rpc shutdown)
В качестве PC_FOR_SHUTDOWN может выступать IP-адрес, DNS-имя
компьютера, или номер кабинета (237, 239).

Скрипт запрашивает пароль для указанного пользователя.
"""

use = "%prog [Options] PC_FOR_SHUTDOWN username[@domain]"

from optparse import OptionParser
from subprocess import call
import getpass


def shutdown(ip, username, password):
    """Shutting down remote windows PCs"""
    cmd = 'net rpc shutdown -f -I %s -U ' % ip + username + '%' + password
    call(cmd, shell = True)


def main():
    parser = OptionParser(description=desc,
                          prog="pc_down.py",
                          version="pc_down.py\nVersion 0.1a",
                          usage=use
                          )
    (options, args) = parser.parse_args()
    if len(args) == 2:
        password = getpass.getpass()
        if args[0] == '237':
            for i in range(101, 121):
                shutdown("192.168.0.%s" % i, args[1], password)
        elif args[0] == '239':
            for i in range(121, 139):
                shutdown("192.168.0.%s" % i, args[1], password)
        else:
            shutdown(args[0], args[1], password)
    else:
        parser.print_help()
    return None


if __name__ == '__main__':
    main()
