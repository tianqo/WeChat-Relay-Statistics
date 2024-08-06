import os
import shutil

# 询问用户输入UUID
#uuid_input = input("请输入UUID: ")
# 打开文件并读取所有行
file_path = input("请复制接龙文档的绝对路径：")
#with open('UUID/yourfile.txt', 'r', encoding="UTF-8") as file:
#    lines = file.readlines()
with open(file_path, 'r', encoding="UTF-8") as file:
    lines = file.readlines()

# 检查是否有足够的行数
if len(lines) >= 2:
    # 获取第二行
    second_line = lines[1]
    # 去除行尾的换行符
    second_line = second_line.strip()

    # 假设UUID在行末，并且用空格或制表符与前面的文本分隔
    # 你可以根据需要调整这个分隔符
    uuid_part = second_line.rsplit(None, 1)[-1]  # 从右侧分割，取最后一个部分

    # 检查提取的部分是否符合UUID的格式
    # UUID通常是32个十六进制数字和4个连字符组成的字符串
    # 这里是一个简单的检查，你可以根据需要添加更严格的验证
    if len(uuid_part) == 36 and all(c in '0123456789abcdef-' for c in uuid_part):
        print("提取到的UUID:", uuid_part)
    else:
        print("未找到有效的UUID")
else:
    print("文件行数不足,检查文档是否少复制或有其他缺漏")

#小文件识别
'''
import re  
  
# UUID的正则表达式模式  
uuid_pattern = re.compile(  
    r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-'  
    r'[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'  
)  
  
# 打开txt文件并读取内容  
with open('yourfile.txt', 'r', encoding='utf-8') as file:  
    content = file.read()  
  
# 使用正则表达式查找所有UUID  
uuids = uuid_pattern.findall(content)  
  
# 输出找到的UUID  
for uuid in uuids:  
    print(uuid)
'''
#大文件识别（部分替换）
'''
with open('yourfile.txt', 'r', encoding='utf-8') as file:  
    for line in file:  
        uuids = uuid_pattern.findall(line)  
        for uuid in uuids:  
            print(uuid)
'''

# 定义uuids目录的路径
uuids_directory = 'code/UUID/uuids'

# 构建完整路径
uuid_path = os.path.join(uuids_directory, uuid_part + ".txt")

# 检查UUID对应的文件或目录是否存在
if os.path.exists(uuid_path):

    # 获取根目录的路径
    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建目标文件的路径，即在根目录下命名为 yourfile.txt
    target_file_path = os.path.join(current_script_dir, 'yourfile.txt')

    # 尝试删除已经存在的yourfile.txt文件
    try:
        if os.path.exists(target_file_path):
            os.remove(target_file_path)
            print(f"已删除文件: {target_file_path}")
    except Exception as e:
        print(f"删除文件时发生错误: {e}")
        # 如果删除失败，你可以选择继续执行复制操作或退出脚本
        # 这里我们选择继续执行复制操作

    # 使用 shutil.copy2 来复制文件到根目录
    try:
        shutil.copy2(file_path, target_file_path)
        print(f"文件已成功从 {file_path} 复制到 {target_file_path}")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")

else:
    print("没有找到相对应的uuid，是否输入有误亦或者uuid过期？")