#!/usr/bin/env python
# -*- coding: utf-8 -*-

desc = """Выключение удаленных ПК под управлением Windows.
Зависимости: Python3, Samba (для net rpc shutdown)
В качестве PC_FOR_SHUTDOWN может выступать IP-адрес, DNS-имя
компьютера, или номер кабинета (237, 239).

Скрипт запрашивает пароль для указанного пользователя.
"""

# Команда выключения с параметрами
cmd = 'net rpc shutdown -f -t 20 \
-C "Извините, компьютер выключается... Не забудьте сохранить Ваши данные."'

from optparse import OptionParser
from subprocess import call
import getpass


def shutdown(pc, username, password, print_only=False):
    """Shutting down remote windows PCs"""
    import ipaddress

    if '-' in pc:
        a, b = pc.split('-')
        ip_first, ip_last = ipaddress.ip_address(a), ipaddress.ip_address(b)
    else:
        ip_first = ip_last = ipaddress.ip_address(pc)

    while ip_first <= ip_last:
        cmd_full = cmd + ' -I %s -U %s%%%s &' % (ip_first, username, password)
        ip_first += 1
        if print_only:
            print(cmd_full)
        else:
            call(cmd_full, shell=True)
    return None


def main():
    use = "%prog [Options] PC_FOR_SHUTDOWN [DOMAIN/]USERNAME"
    parser = OptionParser(description=desc,
                          prog="pc-down.py",
                          version="%prog\nVersion 0.5",
                          usage=use
                          )
    parser.add_option('-p', '--print', default=False, action='store_true',
                      help='только вывод на экран команд выключения ПК')
    (options, args) = parser.parse_args()
    #print(options, args)
    if len(args) == 2:
        password = getpass.getpass()
        if args[0] == '233':
            pc = '192.168.0.51-192.168.0.68'
        elif args[0] == '237':
            pc = '192.168.0.101-192.168.0.120'
        elif args[0] == '239':
            pc = '192.168.0.121-192.168.0.138'
        else:
            pc = args[0]
        shutdown(pc, args[1], password, options.print)
    else:
        parser.print_help()
    return None


if __name__ == '__main__':
    main()
