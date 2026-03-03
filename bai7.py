m = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
x = int(input("Nhập số cần tìm: "))
vi_tri = -1
for i in range(len(m)):
    if m[i] == x:
        vi_tri = i
        break

if vi_tri != -1:
    print("Tìm thấy tại vị trí:", vi_tri)
else:
    print("Chỉ nhập các số nguyên hợp lệ")
