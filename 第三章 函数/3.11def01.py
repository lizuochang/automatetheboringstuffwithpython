"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 7:48 
# @File    : 3.11def01.py
# @Author  : li
# @Software: PyCharm
"""
"""
Collatz 序列
编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
那么 collatz()就打印出 number // 2， 并返回该值。如果 number 是奇数， collatz()就打
印并返回 3 * number + 1。
然后编写一个程序， 让用户输入一个整数， 并不断对这个数调用 collatz()， 直
到函数返回值１（令人惊奇的是， 这个序列对于任何整数都有效， 利用这个序列，
你迟早会得到 1！ 既使数学家也不能确定为什么。 你的程序在研究所谓的“Collatz
序列”，它有时候被称为“最简单的、 不可能的数学问题”）。
"""
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
try:
    number=int(input("Please enter number:"))
    while collatz(number) != 1:
        number = collatz(number)
except:
    print("error")
