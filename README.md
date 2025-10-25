# Algorithms
This covers all the alogrithms a software engineer needs to know


# Merge Sort
Merge Sort is a divide-and-conquer algorithm that works by recursively breaking down a list into smaller sublists until each sublist contains only one element, then repeatedly merging the sublists to produce new sorted sublists until there is only one sorted list remaining.

**Divide Phase:**<br>
[38, 27, 43, 3, 9, 82, 10]<br>
[38, 27, 43] [3, 9, 82, 10]<br>
[38] [27, 43] [3, 9] [82, 10]<br>
[38] [27] [43] [3] [9] [82] [10]<br>

**Merge Phase:**<br>
[27, 38] [43] [3, 9] [10, 82]  
[27, 38, 43] [3, 9, 10, 82]  
[3, 9, 10, 27, 38, 43, 82]  

**Time Complexity**
- Best Case: O(n log n)<br>
- Average Case: O(n log n)<br>
- Worst Case: O(n log n)<br>

**Space Complexity**
- O(n) - requires additional space for temporary arrays<br>

**When to Use Merge Sort**<br>
***Good for:***<br>
- Large datasets<br>
- When stability is important<br>
- External sorting (data doesn't fit in RAM)<br>
- Linked lists (can be implemented with O(1) extra space)<br>
***Less ideal for:***<br>
- Small arrays (overhead of recursion)<br>
- Memory-constrained environments<br>
- When you need an in-place sort<br>