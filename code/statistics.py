# 测试程序可行性
# 用于对已经排序玩的excel文件进行统计
import os
import csv
import jieba
# 定义路径
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

txt1 = jieba.cut(txt)
# 统计词频
counts = {}
for word in txt1:
    if len(word) > 1:
        counts[word] = counts.get(word, 0) + 1

#去停用词
stopwords = set()
with open("code/scu_stopwords.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip("\n")
        if len(line) > 0:
            stopwords.add(line)
counts_new = {}
for word, count in counts.items():
    if word not in stopwords:
        counts_new[word] = count

#提取频次最多的那个词
max_count = 0
for word, count in counts.items():
    if max_count < count:
        max_count = count
        max_word = word

print("请问你是否要统计“"+max_word+"”与否？")

y = 0
n = 0
i = 0

txt2 = jieba.lcut(txt)

while True:
    ans = input("请输入y/n：")
    if ans == "y":
        with open("code/denyword.txt", "r", encoding="UTF-8") as f:
        #在未经过停用词过滤前，统计该词词频
            denyword = f.read().splitlines()
        while len(txt2) - 1 > i:
            if txt2[i] in denyword and txt2[i+1] == max_word:
                n += 1
                i += 2
            elif txt2[i] == max_word:
                y += 1
                i += 1
            else:
                i += 1
        t = y + n
        break
    elif ans == "n":
        print("请输入你想要统计的词：（填入格式请见readme.md）")
        while True:
            max_word = input()
        break