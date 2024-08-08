import os
import csv
import jieba

csv_path = "output.csv"
txt_path = "code/UUID/yourfile.txt"

if os._exists(txt_path):
    os.remove(txt_path)

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    with open(txt_path, "w", encoding="utf-8") as f1:
        for row in reader:
            if len(row) > 1:
                f1.write(row[1] + "\n")

with open(txt_path, "r", encoding="UTF-8") as f:
    txt = f.read()

txt1 = list(jieba.cut(txt))
i = 0
while i < len(txt1):
    print(txt1[i])
    i += 1