"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/16 9:19 
# @File    : 7.18re02.py
# @Author  : li
# @Software: PyCharm
"""

import re

def stripRe(text,word=""):
    """
    写一个函数，它接受一个字符串， 做的事情和 strip()字符串方法一样。如果只
    传入了要去除的字符串， 没有其他参数， 那么就从该字符串首尾去除空白字符。否
    则， 函数第二个参数指定的字符将从该字符串中去除。
    :return:
    """

    if word == '':
        word = ' '
        #只去掉两边的空格
        stripRegex = re.compile(r'^\s*|\s*$')
        mo = stripRegex.sub("",text)
        print(mo)
        print('_______________')
    else:
        print(f'你输入的是：{word}')
        stripRegex = re.compile(f'{word}')
        print(stripRegex.sub('',text))
text="  8how old are you."
stripRe(text)
stripRe(text,"o")
