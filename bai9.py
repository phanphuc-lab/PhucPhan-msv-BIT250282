def in_so_le():
    try:
        data = input("Nhập các số nguyên (cách nhau bởi dấu cách): ")
        numbers = [int(x) for x in data.split()]

        so_le = [n for n in numbers if n % 2 != 0]
        if so_le:
            print("Các số lẻ tìm thấy:", so_le)
        else:
            print("Không có số lẻ nào trong danh sách")

    except ValueError:
        print("Chỉ nhập các số nguyên hợp lệ")
in_so_le()
