def bubble_sort_with_count(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Hoán đổi phần tử
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return arr, count
nums = [36, 35, 18, 15, 37, 28, 1000]
sorted_nums, total_swaps = bubble_sort_with_count(nums)

print("Danh sách sau khi sắp xếp:", sorted_nums)
print("Số lần hoán đổi:", total_swaps)
