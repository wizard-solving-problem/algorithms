# Algorithms
This covers all the alogrithms a software engineer needs to know


# Merge Sort
Merge Sort is a divide-and-conquer algorithm that works by recursively breaking down a list into smaller sublists until each sublist contains only one element, then repeatedly merging the sublists to produce new sorted sublists until there is only one sorted list remaining.

### Divide Phase
[38, 27, 43, 3, 9, 82, 10]  
[38, 27, 43] [3, 9, 82, 10]  
[38] [27, 43] [3, 9] [82, 10]  
[38] [27] [43] [3] [9] [82] [10]  

### Merge Phase
[27, 38] [43] [3, 9] [10, 82]  
[27, 38, 43] [3, 9, 10, 82]  
[3, 9, 10, 27, 38, 43, 82]  

### Time Complexity
- Best Case: O(n log n)  
- Average Case: O(n log n)  
- Worst Case: O(n log n)  

### Space Complexity
- O(n) – requires additional space for temporary arrays  

### When to Use Merge Sort
**Good for:**
- Large datasets  
- When stability is important  
- External sorting (data doesn't fit in RAM)  
- Linked lists (can be implemented with O(1) extra space)  

**Less ideal for:**
- Small arrays (overhead of recursion)  
- Memory-constrained environments  
- When you need an in-place sort  



# Quick Sort (In-place)
Quick Sort is a divide-and-conquer algorithm:  
1. Pick a pivot element.  
2. Partition the array so that:  
    - Elements smaller than the pivot go to its left.  
    - Elements larger than the pivot go to its right.  
3. Recursively apply the same process to the left and right sides.  

The “in-place” part means we do this without using extra arrays — we rearrange the elements within the same array.  
Quick Sort doesn’t directly “sort” all the elements. Instead, it keeps putting pivots in their correct positions.  

### Time Complexity
- Best Case: O(n log n)  
- Average Case: O(n log n)  
- Worst Case: O(n^2)  

### Space Complexity
- O(log n) – recursion stack (in-place partitioning).  






# Binary Search
Binary search is an efficient algorithm for finding an item in a sorted list by repeatedly dividing the search interval in half.  

### How It Works
Imagine you're looking for a word in a dictionary:  
- You don't start at page 1  
- You open to the middle and check if your word comes before or after  
- You eliminate half the remaining pages and repeat  

### Steps
1. Start with the entire sorted array  
2. Find the middle element  
3. Compare the middle element with your target:  
    - If they match: Success! Return the index  
    - mIf target < middle: Search the left half  
    - If target > middle: Search the right half  
4. Repeat until found or the search space is empty  





# Two Pointers
Two Pointers uses two references (pointers) that traverse a data structure (usually an array or string) to solve problems in O(n) time instead of O(n²). Works on sorted array

### Common Patterns
1. **Opposite Direction Pointers:**
Pointers start at both ends and move toward each other.  
Example: Two Sum in Sorted Array  
2. **Same Direction Pointers:**
Both pointers start at the beginning and move in the same direction.  
Example: Remove Duplicates from Sorted Array  
3. **Fast and Slow Pointers:**
One pointer moves faster than the other.   
Example: Linked List Cycle Detection  

### When to Use Two Pointers
Use this technique when you need to:
- Find pairs/triplets in sorted arrays
- Remove duplicates
- Check palindromes
- Merge sorted arrays
- Find subarrays with certain properties

### Time & Space Complexity
- Time Complexity: Usually O(n) - much better than brute force O(n²)
- Space Complexity: O(1) - only using a few pointers