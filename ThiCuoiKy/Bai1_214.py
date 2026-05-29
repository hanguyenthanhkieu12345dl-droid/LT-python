# Nhập chiều dài, chiều rộng, chiều cao
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))

# Nhập số lượng số lẻ cần hiển thị
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính diện tích đáy
dien_tich_day = dai * rong

# Tính thể tích
the_tich = dien_tich_day * cao

# Xuất kết quả
print("Diện tích đáy hình chữ nhật =", round(dien_tich_day, so_le), "cm\u00b2")
print("Thể tích hình khối =", round(the_tich, so_le), "cm\u00b3")