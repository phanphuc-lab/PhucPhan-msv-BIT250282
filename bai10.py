m = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
tong = 0
print("Các số chẵn là:")
for so in m:
    if so % 2 == 0:
        print(so)
        tong += so

print("Tổng các số chẵn là:", tong)
