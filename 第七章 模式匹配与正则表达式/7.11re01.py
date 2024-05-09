"""
不区分大小写的匹配
通常， 正则表达式用你指定的大小写匹配文本。
但是，有时候你只关心匹配字母，不关心它们是大写或小写。要让正则表达式
不区分大小写，可以向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数。

"""
import re

robocop = re.compile(r'robocop', re.I)
mo=robocop.search('RoboCop is part man, part machine, all cop.')

print(mo)