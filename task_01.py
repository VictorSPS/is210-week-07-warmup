#!/usr/bin/env python
# -*- coding: utf-8 -*
""" Fibonacci Sequence."""


def fibonacci(maxint):
    """Generating a fibonacci sequence.
    Arg:
       maxint(int): the upper bound of the loop
    Return:
       LIST(int):a list of newly generated integers - Fibonacci sequence.
    Examples:
       >>> import task_01
       >>> task_01.fibonacci(10)
       [0, 1, 1, 2, 3, 5, 8]
    """
    lastnum, curnum = 0, 1
    list1 = [lastnum]
    while curnum < maxint:
        lastnum, curnum = curnum, lastnum + curnum
        list1.append(lastnum)
    return list1
