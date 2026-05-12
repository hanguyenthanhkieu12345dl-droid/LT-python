tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

a = int(input("Nhập số tiền cần trả: "))
b = int(input("Nhập số tiền khách đưa: "))

if a > b:
    print("\nKhách còn thiếu:", a - b)
    print("Cảm ơn khách hàng. Hẹn gặp lại!")

elif a == b:
    print("\nCảm ơn khách hàng. Hẹn gặp lại!")

else:
    tien_thoi = b - a
    tong_to = 0
    tong_loai = 0

    print("\nSố tiền cần thối lại là:", tien_thoi)
    print("Đổi thành:")

    for loai in tien:
        so_to = tien_thoi // loai
        tien_thoi = tien_thoi % loai

        # Chỉ in loại tiền có số tờ > 0
        if so_to > 0:
            print(f"Loại {loai} gồm {so_to} tờ")
            tong_loai += 1

        tong_to += so_to

    print("\nTỔNG CỘNG CÓ", tong_to, "TỜ")
    print("Tổng số loại =", tong_loai)

    print("\nCảm ơn khách hàng. Hẹn gặp lại!")

print("\n===== TEST a > b =====")
a = 1000
b = 800

if a > b:
    print("Khách còn thiếu:", a - b)
    print("Cảm ơn khách hàng. Hẹn gặp lại!")

print("\n===== TEST a == b =====")
a = 1000
b = 1000

if a == b:
    print("Cảm ơn khách hàng. Hẹn gặp lại!")

print("\n===== TEST a < b =====")
a = 766
b = 2000

if a < b:
    tien_thoi = b - a
    tong_to = 0
    tong_loai = 0

    print("Số tiền cần thối lại là:", tien_thoi)
    print("Đổi thành:")

    for loai in tien:
        so_to = tien_thoi // loai
        tien_thoi = tien_thoi % loai

        if so_to > 0:
            print(f"Loại {loai} gồm {so_to} tờ")
            tong_loai += 1

        tong_to += so_to

    print("TỔNG CỘNG CÓ", tong_to, "TỜ")
    print("Tổng số loại =", tong_loai)

    print("Cảm ơn khách hàng. Hẹn gặp lại!")