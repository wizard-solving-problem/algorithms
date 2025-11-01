def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target: return [left, right]
        elif current_sum < target: left += 1
        else: right -= 1
    return [-1, -1]  



arr = [2, 7, 11, 15, 20]
target = 22
print(two_sum_sorted(arr, target))
