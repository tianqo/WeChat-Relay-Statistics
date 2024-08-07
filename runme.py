#**coding:utf-8**
import sys
from prettytable import PrettyTable
 
table = PrettyTable(['快捷键','执行程序'])
table.add_row(['a','txt文档分类统计'])
table.add_row(['b','接龙计数统计'])
print(table)
print("如果你不清楚要执行哪个程序，请仔细阅读readme文件后再执行。")
user_input = input("请输入你要执行的程序")
# 检测用户输入内容并返回相应执行程序
if user_input.lower() == 'a':
        import subprocess
        subprocess.run(['python', 'code/logic.py'])
        sys.exit()
elif user_input.lower() == 'b':
        import subprocess
        subprocess.run(['python', 'code/statistics.py'])
        sys.exit()
else:
        print("输入错误，请重新输入！")