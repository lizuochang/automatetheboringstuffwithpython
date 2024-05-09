"""
项目： 电话号码和 E-mail 地址提取程序
如果有一个程序， 可以在剪贴
板的文本中查找电话号码和 E-mail 地址， 那你就只要按一下 Ctrl-A 选择所有文本，
按下 Ctrl-C 将它复制到剪贴板， 然后运行你的程序。它会用找到的电话号码和 E-mail
地址， 替换掉剪贴板中的文本
"""

import re, pyperclip

# 第 1 步： 为电话号码创建一个正则表达式

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code “可选的” 区号
    (\s|-|\.)?                   # separator 电话号码分割字符可以是空格（\s）、 短横（-） 或句点（.）
    (\d{3})                      # first 3 digits
    (\s|-|\.)                    # separator
    (\d{4})                      # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension 任意数目的空格，接着 ext、 x 或 ext.， 再接着 2 到 5 位数字。
    )''', re.VERBOSE)
# TODO: Create email regex.
# 第 2 步： 为 E-mail 地址创建一个正则表达式

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)
# TODO: Find matches in clipboard text.
# 第 3 步：在剪贴板文本中找到所有匹配

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')