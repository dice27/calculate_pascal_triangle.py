#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

def print_pascal_triangle():
    print ('Enter number of rows:')
    row = raw_input('>>>  ')
    if not row.isdigit():
        print ('[Err] Please enter half-width numeric characters.')
        return

    triangle = []
    triangle.append(1)
    print(triangle)

    for i in range(int(row)-1):
        prev = copy.deepcopy(triangle)
        del triangle[:]
        triangle.append(1)

        for j in range(1,len(prev)):
            triangle.append(prev[j-1] + prev[j])

        triangle.append(1)
        print(triangle)

if __name__ == '__main__':
    print_pascal_triangle()
