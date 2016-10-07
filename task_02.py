#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Function that can return Yes or No value"""


def bool_to_str(bval):
    """Function takes only one argument, uses if else statement
       and return a string.
    Arg:
       bval(boolean): value that can be evaluated for truth or false
    Return:
       var(str): returns a string Yes if bval is True, No if False
    Examples:
       >>> import task_02
       >>> task_02.bool_to_str(True)
       'Yes'
       >>> import task_02
       >>> task_02.bool_to_str('')
       'No'
    """

    if bval:
        var = 'Yes'
    else:
        var = 'No'
    return var
