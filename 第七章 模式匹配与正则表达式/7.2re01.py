"""
虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
1． 用 import re 导入正则表达式模块。
2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串
"""


import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())