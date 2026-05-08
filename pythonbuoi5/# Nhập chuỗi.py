# Nhập chuỗi
S = input("Nhập chuỗi: ")

# Tách các từ trong chuỗi
words = S.split()

# Tìm từ đầu tiên lặp lại
lap = None

for i in words:
    if words.count(i) > 1:
        lap = i
        break

# In kết quả
print("Từ đầu tiên lặp lại là:", lap)