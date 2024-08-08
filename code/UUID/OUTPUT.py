import os  
<<<<<<< HEAD
  
# 生成一个基于随机数的UUID  
random_uuid = uuid.uuid4()  
  
# 定义保存UUID的目录  
directory = 'code/UUID/uuids'
if not os.path.exists(directory):  
    os.makedirs(directory)  
  
# 生成文件名，这里简单地使用UUID的字符串形式作为文件名  
filename = str(random_uuid) + '.txt'  
file_path = os.path.join(directory, filename)  
  
# 将UUID保存到文件中  
with open(file_path, 'w') as file:  
    file.write(str(random_uuid))  
  
print(f"你的UUID为：{random_uuid} 请将此UUID黏贴于微信接龙备注末尾\n\nUUID若遗忘，文件保存在 {file_path} 中\n\n注意：若无法找回UUID可以重新生成一条新的UUID重新放置于备注末尾")
=======

folder_path = "txt-collection"  
txt_files = {}
if not os.path.exists("code/UUID/uuids"):
    os.makedirs("code/UUID/uuids")
# 列举所有存放在txt-collection文件夹中的txt文件,并为每个文件标上序号以便用户选择
# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否是txt文件
    if filename.endswith('.txt'):
        # 获取文件的完整路径
        file_path = os.path.join(filename)
        # 这里假设我们直接用序号来标记，从1开始
        # 注意：os.listdir()返回的文件名列表顺序依赖于操作系统，可能不是按文件名排序的
        txt_files[len(txt_files) + 1] = file_path

# 打印出所有txt文件及其序号
for index, file_path in txt_files.items():
    print(f"{index}: {file_path}")

user_choice = input("请输入要选择的文件的序号: ")
if user_choice.isdigit() and int(user_choice) in txt_files:
    selected_file = txt_files[int(user_choice)]
    selected_path = os.path.join(folder_path, selected_file)
    print(f"您选择的文件是: {selected_file}")
    #print(f"文件路径是: {selected_path}")
else:
    print("无效的序号，请重新输入！")

# 执行安全路径复制
with open(selected_path, 'r', encoding="UTF-8") as file:
    lines = file.readlines()

# 检查是否有足够的行数
if len(lines) >= 2:
    # 获取第二行
    second_line = lines[1]
    # 去除行尾的换行符
    second_line = second_line.strip()
else:
    print("文件行数不足,检查文档是否少复制或有其他缺漏")



# 安全路径
# 将选择的文件复制到UUID文件夹中，并重命名为yourfile.txt
#首先检测UUID文件夹是否已经存在yourfile.txt文件，有的话事先删除
i = 0
while i<1:
    if os.path.exists("code/UUID/yourfile.txt"):
        os.remove("code/UUID/yourfile.txt")
        
    else:
        import shutil
        shutil.copy(selected_path, "code/UUID/yourfile.txt")
        i = 1

>>>>>>> test
