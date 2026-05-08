try:
    f = open(r"C:\Users\DELL\Documents\pythonbuoi5\test.txt", "r", encoding="utf-8")
    text = f.read()
    f.close()

    compressed = " ".join(text.split())

    f = open(r"C:\Users\DELL\Documents\pythonbuoi5\compressed.txt", "w", encoding="utf-8")
    f.write(compressed)
    f.close()

    print("Nội dung sau khi giảm dung lượng:")
    print(compressed)

    f = open(r"C:\Users\DELL\Documents\pythonbuoi5\compressed.txt", "r", encoding="utf-8")
    data = f.read()
    f.close()

    restored = data.replace(". ", ".\n")

    f = open(r"C:\Users\DELL\Documents\pythonbuoi5\restore.txt", "w", encoding="utf-8")
    f.write(restored)
    f.close()

    print("\nNội dung sau khi khôi phục:")
    print(restored)

except FileNotFoundError:
    print("Không tìm thấy file")

except Exception as e:
    print("Lỗi:", e)