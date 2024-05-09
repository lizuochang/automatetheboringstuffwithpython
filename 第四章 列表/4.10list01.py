"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 14:59 
# @File    : 4.10list01.py
# @Author  : li
# @Software: PyCharm
"""
"""
逗号代码
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将
前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
该能够处理传递给它的任何列表。
"""

spam = ['apples', 'bananas', 'tofu', 'cats']

def concatelist(spam):
    strout = ""
    for strnum in range(len(spam)-1):
        strout=strout+spam[strnum]+","
    strout = strout + "and" + " "+spam[len(spam)-1]
    return strout

print(concatelist(spam))