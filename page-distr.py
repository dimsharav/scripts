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
    usage = '%prog [Options] begin_page end_page'
    version = '0.2'
    p = optparse.OptionParser(description=description,
                              prog=prog,
                              usage=usage,
                              version=version)
    opts, args = p.parse_args()
    if False:   # TODO
        pass
    else:
        p.print_help()
        sys.exit()
    is_list, page_from, page_to = 1, 1, 8
    return is_list, page_from, page_to


def create_book(page_from, page_to):
    # TODO: Переделать
    pages_even = []
    pages_odd = []
    for i in range(page_from, page_to + 1, 4):
        print(i)
        pages_even.append(page_to - i)
        pages_even.append(page_from + i)
        pages_odd.append(page_from + i + 1)
        pages_odd.append(page_to - i - 1)
    #for i in range(0, len(pages_odd) // 2, 2):
        #j = len(pages_odd) - i
        #pages_odd[i], pages_odd[j - 2] = pages_odd[j - 2], pages_odd[i]
        #pages_odd[i + 1], pages_odd[j - 1] = pages_odd[j - 1], pages_odd[i + 1]
    return pages_even, pages_odd


def create_list(page_from, page_to):
    pages_even = []
    pages_odd = []
    for i in range(page_from, page_to + 1, 4):
        pages_even.append(i)
        pages_even.append(i + 1)
        pages_odd.append(i + 2)
        pages_odd.append(i + 3)
    for i in range(0, len(pages_odd) // 2, 2):
        j = len(pages_odd) - i
        pages_odd[i], pages_odd[j - 2] = pages_odd[j - 2], pages_odd[i]
        pages_odd[i + 1], pages_odd[j - 1] = pages_odd[j - 1], pages_odd[i + 1]
    return pages_even, pages_odd


if __name__ == '__main__':
    is_list, page_from, page_to = parser()
    if is_list:
        pages_even, pages_odd = create_list(page_from, page_to)
    else:
        pages_even, pages_odd = create_book(page_from, page_to)
    print('Нечетные листы:\n%s\nЧетные листы:\n%s' % (pages_even, pages_odd))
