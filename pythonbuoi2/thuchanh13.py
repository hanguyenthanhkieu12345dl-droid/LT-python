import re

# Nhập nhiều dòng (giống bài thơ)
print("Nhập chuỗi (Enter nhiều dòng, Ctrl+D/Ctrl+Z để kết thúc):")
lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except:
        break

result = []

for line in lines:
    # 1. Bỏ khoảng trắng đầu/cuối
    line = line.strip()

    # 2. Chỉ giữ 1 khoảng trắng giữa các từ
    line = re.sub(r'\s+', ' ', line)

    # 3. Xóa khoảng trắng trước dấu . ,
    line = re.sub(r'\s+([,.])', r'\1', line)

    result.append(line)

# In kết quả
print("\nChuỗi hoàn chỉnh:")
for line in result:
    print(line)