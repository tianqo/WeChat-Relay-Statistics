# 测试程序可行性
# 用于对已经排序玩的excel文件进行统计
import os
import pandas as pd
import jieba as jb
# 定义路径
csv_path = "code/UUID/output.csv"
txt_path = "code/UUID/yourfile.txt"
#将xlsx文件转换为csv文件并暂存如UUID文件夹中
# 如果csv文件存在则删除
if os.path.exists("code/UUID/output.csv"):
    os.remove("code/UUID/output.csv")
data_xlsx = pd.read_excel("output.xlsx")
data_xlsx.to_csv("code/UUID/output.csv",encoding = 'utf-8')

# 将csv文件的第三列复制入yourfile.txt中
# 如果yourfile.txt存在则删除
if os.path.exists(txt_path):
    os.remove(txt_path)
data = pd.read_csv(csv_path,encoding='utf-8')
data = data.iloc[:,2]
data.to_txt(txt_path,encoding = 'utf-8')