def count_vowels(s):
    dem = 0
    for i in range(len(s)):
        if s[i].lower() in "aeiou":
            dem += 1
    return dem
chuoi = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(chuoi))
