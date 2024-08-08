import os
import sys
import re
import csv
# 定义目录路径
i = 0
if not os.path.exists('code/UUID/uuids'):
    print("这是你第一次使用本程序，请仔细阅读readme文件后使用。")
# 检查目录是否存在
    # 获取用户输入
user_input = input("开始统计？\n请输入 'y' 或 'n': ")

# 使用 if-elif-else 语句检查输入
while i < 1:
    if user_input.lower() == 'y':
        import subprocess
        subprocess.run(["python", "code/UUID/OUTPUT.py"])
        #print("你输入了 '1'。")
        i = 1
    elif user_input.lower() == 'n':
        sys.exit(0)
        i = 1
    else:
         user_input = input("你输入的不是 '1' 也不是 '2'。请重新输入：")

print("开始统计...")
pattern = r'^\d+\.\s+\S+'
i = 0
csv_rows = []
# 从txt文档的第四行开始读取数据
with open('code/UUID/yourfile.txt', 'r', encoding='utf-8') as f:
    for line in f:
        match = re.match(r'^\d+\.\s+(.*)', line)
        if match:
            # match.group(1) 现在包含了序号和点号之后的所有内容
            # 我们进一步按空格分割这部分内容
            sub_parts = match.group(1).split(' ', -1)  # 使用split的maxsplit参数来确保只分割一次
            
            # 现在，sub_parts[0] 是第一列的内容，如果sub_parts有第二个元素，则它是第二列的内容
            if len(sub_parts) > 1:
                csv_rows.append(sub_parts)
            else:
                # 如果只有一个部分，我们可能想要在第二列中放入一个空字符串或占位符
                csv_rows.append([sub_parts[0], ''])
        else:
            # 如果行不匹配我们的模式，我们可以选择忽略它或记录下来
            print(f"忽略不符合条件的行: {line}")

# 写入CSV文件
if os.path.exists('output.csv'):
    os.remove('output.csv')
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # 写入列标题（如果需要）
    # writer.writerow(['Column1', 'Column2'])
    # 写入数据行
    for row in csv_rows:
        writer.writerow(row)

# 最后处理
input_file = 'output.csv'

# 使用csv.reader读取文件
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    lines = infile.readlines()

# 使用文件写入方式写入新文件
with open(input_file, 'w', newline='', encoding='utf-8') as outfile:
    for line in lines:
        # 替换连续的逗号为单个逗号
        cleaned_line = ','.join(filter(None, line.split(','))).strip() + '\n'
        # 写入处理后的行
        outfile.write(cleaned_line)

print(f"内容已填充到csv文件")
