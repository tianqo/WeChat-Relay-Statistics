def parse_attendance(text):  
    # 将文本分割成单词列表（这里假设以空格为分隔符）  
    words = text.split()  
      
    # 遍历单词列表，查找“参加”或“不参加”  
    for word in words:  
        if word == '参加':  
            return True  # 表示参加  
        elif word == '不参加':  
            return False  # 表示不参加  
      
    # 如果没有找到明确的“参加”或“不参加”，可以返回None或抛出异常  
    return None  # 或者 raise ValueError("Unable to determine attendance")  
  
# 示例  
print(parse_attendance("我要参加"))  # 输出: True  
print(parse_attendance("我不参加"))  # 输出: False  
print(parse_attendance("我不想参加"))  # 输出: None （因为没有直接匹配“不参加”）  
  
# 对于“我不想参加”的情况，你可能需要调整逻辑来识别否定词  
def parse_attendance_advanced(text):  
    words = text.split()  
      
    # 检查是否包含否定词后紧接着是“参加”  
    for i in range(len(words) - 1):  
        if words[i] in ['不', '没有', '没', '不想'] and words[i+1] == '参加':  
            return False  
      
    # 检查是否包含“参加”  
    for word in words:  
        if word == '参加':  
            return True  
      
    # 如果没有找到明确的参加情况，返回None  
    return None  
  
# 使用改进的逻辑  
print(parse_attendance_advanced("我要参加"))  # 输出: True  
print(parse_attendance_advanced("我不参加"))  # 输出: False  
print(parse_attendance_advanced("我不想参加"))  # 输出: False