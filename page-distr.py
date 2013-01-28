#!/usr/bin/env python
# -*- coding: utf-8 -*-

description = '''
Распределение страниц для печати по 2 страницы на лист.
Поддерживается 2 вида распределения:
    1) Последовательные страницы:
        1 2  |  3 4
        5 6  |  7 8
    2) Книга (пример из 8 страниц):
        8 1  |  2 7
        6 3  |  4 5
После распечатки нечетных страниц стопку бумаги переложить во входной лоток,
не изменяя порядок листов.
'''

import optparse
import sys


def parser():
    prog = 'page-distr.py'
    usage = '%prog [options] begin_page end_page'
    version = '0.2'
    p = optparse.OptionParser(description=description,
                              prog=prog,
                              usage=usage,
                              version=version)
    p.add_option('--type', '-t', type='choice', dest='type',
                 help='Тип распределения: list или book. По-умолчанию: list',
                 choices=['list', 'book'],
                 default='list')
    opts, args = p.parse_args()
    if len(args) == 2:
        if opts.type == 'list':
            is_list = True
        else:
            is_list = False
        page_from = int(args[0])
        page_to = int(args[1])
    else:
        p.print_help()
        sys.exit()
    return is_list, page_from, page_to


def change_list_order(list):
    for i in range(0, len(list) // 2, 2):
        j = len(list) - i
        list[i], list[j - 2] = list[j - 2], list[i]
        list[i + 1], list[j - 1] = list[j - 1], list[i + 1]
    return list


def create_book(page_from, page_to):
    pages_even = []
    pages_odd = []
    pages_count = page_to - page_from + 1
    if pages_count % 4 != 0:
        pages_count += (4 - (pages_count % 4))
        page_to = page_from + pages_count - 1
    for i in range(0, pages_count, 4):
        pages_even.append(page_to - i)
        pages_even.append(page_from + i)
        pages_odd.append(page_from + i + 1)
        pages_odd.append(page_to - i - 1)
    return pages_even, change_list_order(pages_odd)


def create_list(page_from, page_to):
    pages_even = []
    pages_odd = []
    for i in range(page_from, page_to + 1, 4):
        pages_even.append(i)
        pages_even.append(i + 1)
        pages_odd.append(i + 2)
        pages_odd.append(i + 3)
    return pages_even, change_list_order(pages_odd)


if __name__ == '__main__':
    is_list, page_from, page_to = parser()
    if is_list:
        pages_even, pages_odd = create_list(page_from, page_to)
    else:
        pages_even, pages_odd = create_book(page_from, page_to)
    print('Нечетные страницы:\n%s\nЧетные страницы:\n%s'\
          % (pages_even, pages_odd))
