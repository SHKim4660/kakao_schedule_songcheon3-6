def add_thing():
    strline = ""
    f = open("C:/Users/shkim/OneDrive - 인천광역시교육청/바탕 화면/2024반톡.txt", 'r', encoding='utf-8')

    while True:
        line = f.readline()
        if not line: break
        strline += line

    return strline

print(add_thing())