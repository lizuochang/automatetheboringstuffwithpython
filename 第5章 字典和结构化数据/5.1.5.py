"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 17:31 
# @File    : 5.1.5.py
# @Author  : li
# @Software: PyCharm
"""
"""
setdefault()方法提供了一种方式，在一行中完成这件事。传递给该方法的第一
个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键
确实存在，方法就会返回键的值。
setdefault()方法是一个很好的快捷方式，可以确保一个键存在。下面有一个小
程序， 计算一个字符串中每个字符出现的次数。
"""
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

