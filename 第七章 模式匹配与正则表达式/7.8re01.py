"""
可以在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文
本开始处。类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必
须以这个正则表达式的模式结束。可以同时使用^和$，表明整个字符串必须匹配该
模式，也就是说，只匹配该字符串的某个子集是不够的。
"""

import re

beginsWithHello = re.compile(r'^Hello')
mo=beginsWithHello.search('Hello world!')

print(mo.group())
print(beginsWithHello.search('He said hello.') == None)

# 正则表达式 r'\d$'匹配以数字 0 到 9 结束的字符串

endsWithNumber = re.compile(r'\d$')
mo=endsWithNumber.search('Your number is 42 a 68')

print(mo)