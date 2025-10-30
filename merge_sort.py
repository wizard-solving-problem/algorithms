def merge_sort(arr):
    return divide_array(arr)


def divide_array(arr):
    if len(arr) <=1: return arr
    
    mid_point = len(arr) // 2
    left = arr[:mid_point]
    right = arr[mid_point:]

    # breaking the array
    left_divide = divide_array(left)
    right_divide = divide_array(right)

    # sorting and merging
    return sort_and_merge(left_divide, right_divide)


def sort_and_merge(left, right):
    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    # append any remaining elements from left and right portions
    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res


arr = [20, 5, 1, 0, -5, 5, 23, 1, 4, 6, 9, -43]
sorted_arr = merge_sort(arr)

print("Original:", arr)
print("Sorted:", sorted_arr)