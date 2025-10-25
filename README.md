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