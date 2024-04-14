import uuid  
import os  
  
# 生成一个基于随机数的UUID  
random_uuid = uuid.uuid4()  
  
# 定义保存UUID的目录  
directory = 'UUID/uuids'
if not os.path.exists(directory):  
    os.makedirs(directory)  
  
# 生成文件名，这里简单地使用UUID的字符串形式作为文件名  
filename = str(random_uuid) + '.txt'  
file_path = os.path.join(directory, filename)  
  
# 将UUID保存到文件中  
with open(file_path, 'w') as file:  
    file.write(str(random_uuid))  
  
print(f"你的UUID为：{random_uuid} 请将此UUID黏贴于微信接龙备注末尾\n\nUUID若遗忘，文件保存在 {file_path} 中\n\n注意：若无法找回UUID可以重新生成一条新的UUID重新放置于备注末尾")