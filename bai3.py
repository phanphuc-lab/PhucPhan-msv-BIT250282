danh_sach_mau = ["đỏ", "xanh", "hồng", "vàng", "tím"]
try:
    danh_sach_mau.remove("hồng")
except ValueError:
    print("Màu 'hồng' không có trong danh sách.")
print("Danh sách sau khi xử lý:", danh_sach_mau)
