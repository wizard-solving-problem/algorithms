def quick_sort (arr, low, high):
    sorting(arr, low, high)


def partition_and_sort (arr, low, high):
    # this the reference value
    pivot = arr[high]
    # starting with just below "low" so that when the if condition meets
    # the smaller than pivot value goes into the right position
    i = low - 1
    for j in range (low, high): # the loop does not touch pivot value
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # place the pivot after the smaller section
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # new pivot index
    return i + 1


def sorting (arr, low, high):
    # Only sort if there’s more than one element in this part of the array.
    # Eventually, you’ll reach a situation where:
    # low == high → there’s only one element, or
    # low > high → the subarray is empty.
    # In both cases, that part is already sorted — nothing left to do.
    if low < high:
        partition_idx = partition_and_sort(arr, low, high)
        # (partion_idx - 1) because we do not need to sort the pivot itself
        sorting(arr, low, partition_idx - 1) 
        sorting(arr, partition_idx + 1, high)




arr = [20, 5, 1, 0, -5, 5, 23, 1, 4, 6, 9, -43]
print("Original:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted:", arr)