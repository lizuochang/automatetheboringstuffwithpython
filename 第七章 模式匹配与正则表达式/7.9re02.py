"""
用句点字符匹配换行
点-星将匹配除换行外的所有字符。通过传入 re.DOTALL 作为 re.compile()的第
二个参数， 可以让句点字符匹配所有字符， 包括换行字符。
"""
import re

str='Serve the public trust.\nProtect the innocent.\nUphold the law.'
noNewlineRegex = re.compile('.*')

mo1=noNewlineRegex.search(str)

print(mo1)
newlineRegex = re.compile('.*', re.DOTALL)
mo2=newlineRegex.search(str)
print(mo2.group())