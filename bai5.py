def insertion_sort_descending():
    try:
        data = input("Nhập các số thực, cách nhau bởi dấu cách: ")
        numbers = [float(x) for x in data.split()]
        for i in range(1, len(numbers)):
            key = numbers[i]
            j = i - 1
            while j >= 0 and numbers[j] < key:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key
        print("Kết quả sắp xếp giảm dần:", numbers)
    except ValueError:
        print("Vui lòng chỉ nhập các chữ số hợp lệ")
insertion_sort_descending()
