
"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/16
# @Author  : li
# 测试数据： abcAdB123 复制到剪贴板
"""
"""
写一个函数，它使用正则表达式， 确保传入的口令字符串是强口令。 强口令的
定义是： 长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字。你可
能需要用多个正则表达式来测试该字符串， 以保证它的强度。
"""
import pyperclip, re
text = str(pyperclip.paste())


def testing(text):
    if len(text) <= 8:
        return False
    number1 = re.compile(r'\d+')
    if number1.search(text) == None:
        return False
    number2 = re.compile(r'[A-Z]+')
    if number2.search(text) == None:
        return False
    number3 = re.compile(r'[a-z]+')
    if number3.search(text) == None:
        return False
    return True

errorstr="""
         Make sure the password-string is a strong one.
         A strong password is defined as one that is at least eight characters long,
         contains both uppercase and lowercase characters, and contains at least one digit.
"""
a = testing(text)
if a:
    print("ok!")
else:
    print(errorstr)
