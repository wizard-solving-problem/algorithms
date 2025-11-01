def remove_duplicates_from_sorted_array_length(arr):
    if not arr: return 0

    slow = 0 # position for next unique element. also the eventual length of unique elements in the array
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]: 
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1 # coz it started from 0, so the length is 1 extra.

arr = [1, 2, 2, 2, 2, 3, 4, 4, 5]
print("Before:", arr)
new_length = remove_duplicates_from_sorted_array_length(arr)
print(f"New length: {new_length}")
print(f"Array: {arr[:new_length]}")