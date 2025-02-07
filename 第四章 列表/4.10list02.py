"""
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 10:16 
# @File    : 4.10list02.py
# @Author  : li
# @Software: PyCharm
"""
"""
字符图网格
假定有一个列表的列表， 内层列表的每个值都是包含一个字符的字符串， 像这样：
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
你可以认为 grid[x][y]是一幅“图” 在 x、 y 坐标处的字符， 该图由文本字符组
成。 原点(0, 0)在左上角， 向右 x 坐标增加， 向下 y 坐标增加。
复制前面的网格值， 编写代码用它打印出图像。
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
提示 你需要使用循环嵌套循环，打印出 grid[0][0]，然后 grid[1][0]，然后 grid[2][0]，以此
类推，直到 grid[8][0]。这就完成第一行，所以接下来打印换行。然后程序将打印出
grid[0][1]，然后 grid[1][1]，然后 grid[2][1]，以此类推。程序最后将打印出 grid[8][5]。
而且， 如果你不希望在每次 print()调用后都自动打印换行， 记得向 print()传递
end 关键字参数。
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for r in range(len(grid[0])):
        for c in range(len(grid)):
                print(grid[c][r],end="")
        print()



