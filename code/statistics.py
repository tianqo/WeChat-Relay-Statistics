# 测试程序可行性
# 用于对已经排序玩的excel文件进行统计

#读取output.xlsx文件,并提取关键词
# 统计关键词出现的次数
import xlrd
from collections import Counter
def get_data(file):
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]
    rows = sheet.nrows
    cols = sheet.ncols
    data = []
    for i in range(1, rows):
        row = sheet.row_values(i)
        data.append(row[2])
    return data
def count_words(data):
    word_list = []
    for line in data:
        line = line.replace(" ", "")
        line = line.split(",")
        for word in line:
            if len(word) > 3 and word not in word_list:
                word_list.append(word)
    counter = Counter(word_list)
    print(counter)
    return counter
def main():
    data = get_data('output.xlsx')
    count_words(data)
main()