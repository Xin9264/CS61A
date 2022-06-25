import re


def f(a, b):
    if a > b:
        return f(a - 3, b * 2)
    elif a < b:
        return f(b // 2, a)
    else:
        return b
        