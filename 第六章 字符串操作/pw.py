"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/28 16:20 
# @File    : pw.py
# @Author  : li
# @Software: PyCharm
"""
"""
你希望用一个命令行参数来运行这个程序， 该参数是账号的名称。例如， 账号
的口令将拷贝到剪贴板， 这样用户就能将它粘贴到口令输入框。通过这种方式， 用
户可以有很长而复杂的口令，又不需要记住它们。
"""
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)