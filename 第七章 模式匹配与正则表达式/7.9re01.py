"""
通配字符
在正则表达式中， .（句点）字符称为“通配符”。它匹配除了换行之外的所有
字符。
句点字符只匹配一个字符， 这就是为什么在前面的例子中， flat， 只匹配 lat。要匹配真正的句点， 就是用倒斜杠转义：\.。
"""
import re

atRegex = re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

"""
用点-星匹配所有字符
有时候想要匹配所有字符串。例如，假定想要匹配字符串'First Name:'，接下来
是任意文本，接下来是'Last Name:'，然后又是任意文本。可以用点-星（ .*）表示“任
意文本”。回忆一下，点字符表示“除换行外所有单个字符”，星号字符表示“前
面字符出现零次或多次”。
"""

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo)

"""
点-星使用“贪心” 模式：它总是匹配尽可能多的文本。要用“非贪心” 模式匹配
所有文本， 就使用点-星和问号。像和大括号一起使用时那样， 问号告诉 Python 用非贪
心模式匹配。 看看贪心模式和非贪心模式的区别：
"""

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())