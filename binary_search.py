def binary_search(arr, val): 
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 # interger floor division
        if arr[mid] == val: return True
        elif arr[mid] < val: low = mid + 1
        else: high = mid - 1
    return False

arr = [2, 5, 8, 12, 16, 23, 38, 45]
print("array:", arr)
find_val = input("Enter the value to look for: ")
print(binary_search(arr, int(find_val)))