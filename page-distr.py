#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Распределение страниц для печати по 2 страницы на лист

page-distr.py BEGIN_PAGE END_PAGE
'''


def main(page_from, page_to):
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
    print(main(101, 200))
