import re

# 假设txt_file_path是你要读取的txt文件的路径
txt_file_path = r'D:\01_Kylin\微信接龙小程序统计系统\新建文本文档.txt'  # 替换为你的txt文件路径
# 假设sorted_txt_file_path是排序后txt文件的输出路径
sorted_txt_file_path = 'sorted_output.txt'

# 正则表达式模式，用于匹配序号
pattern = r'^\d+\.'

# 初始化变量来记录上一个序号的行号
prev_line_number = None
count = 0  # 用于记录序号之间的行数
lines_with_numbers = []  # 存储包含序号的行
lines_without_numbers = []  # 存储不包含序号的行

# 读取txt文件内容
with open(txt_file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        if re.match(pattern, line):
            # 如果检测到序号，记录上一个序号的行号并计算count
            if prev_line_number:
                count = line_number - prev_line_number - 1
            prev_line_number = line_number
            lines_with_numbers.append(line)
        else:
            lines_without_numbers.append(line)

        # 对包含序号的行进行排序
sorted_lines_with_numbers = sorted(lines_with_numbers)

# 初始化新的文件内容列表
new_content = []

# 初始化序号生成器
number_generator = iter(range(1, len(sorted_lines_with_numbers) + 1))

# 遍历排序后的包含序号的行
for line in sorted_lines_with_numbers:
    # 提取序号后的第一个空格到第二个空格之间的元素
    match = re.search(r'(\d+)\.\s+(.*?)\s+', line)
    if match:
        element = match.group(2)
        new_content.append(f"{next(number_generator)}. {element}\n")
        # 将序号后的剩余部分作为新的一行写入
        new_content.append(line[match.end():].strip() + '\n')

    # 在序号和没有序号的行之间每隔count+1行插入新的序号
for i, line in enumerate(lines_without_numbers):
    if i % (count + 1) == 0 and i != 0:
        new_content.append(f"{next(number_generator)}. \n")
    new_content.append(line)

# 将新内容写入输出文件
with open(sorted_txt_file_path, 'w', encoding='utf-8') as sorted_file:
    sorted_file.writelines(new_content)

print(f"排序后的内容已保存至: {sorted_txt_file_path}")