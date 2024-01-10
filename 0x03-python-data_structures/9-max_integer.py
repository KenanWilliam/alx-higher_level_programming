#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is None:
        return None
    if not my_list:
        return None
    max_val = float('-inf')
    for i in my_list:
        if isinstance(i, int) and i > max_val:
            max_val = i
    if max_val == float('-inf'):
        return None
    return max_val
