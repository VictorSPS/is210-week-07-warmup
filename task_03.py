#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_03"""

import decimal


def lexicographics(to_analyze):
    """Function takes one parametr, calculates the max, min
       and average of the input string.
    Arg:
       to_analyze(str): the input value of the function.
       text(str):split the input string into new line.
       maxcount(int): max number. of words.
       mincount(int): min number of words.
       average(Decimal): average of input.
    Return:
       returns a tuple containing maxcount, mincount and average.
    Examples:
       >>> import task_03
       >>> task_03.lexicographics('''Don't stop believing,
            Hold on to that feeling.''')
       (5, 3, Decimal('4'))
    """

    text = to_analyze.split('\n')
    list1 = []
    for item in text:
        myvar = len(item.split())
        list1.append(myvar)
        maxcount = max(list1)
        mincount = min(list1)
        average = decimal.Decimal(sum(list1)/decimal.Decimal(len(text)))
    return maxcount, mincount, average
