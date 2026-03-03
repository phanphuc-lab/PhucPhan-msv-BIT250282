try:
    data = input("Nhập danh sách số (cách nhau bởi dấu cách): ")
    numbers = [float(x) for x in data.split()]
    found = False
    for n in numbers:
        if n > 10:
            print(f"Kết quả: {n}")
            found = True
            break

    if not found:
        print("Không có số nào lớn hơn 10.")
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập các chữ số.")
