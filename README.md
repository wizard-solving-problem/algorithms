# algorithms
This covers all the alogrithms a software engineer needs to know


# Merge Sort
Merge Sort is a divide-and-conquer algorithm that works by recursively breaking down a list into smaller sublists until each sublist contains only one element, then repeatedly merging the sublists to produce new sorted sublists until there is only one sorted list remaining.

Divide Phase:
[38, 27, 43, 3, 9, 82, 10]
[38, 27, 43] [3, 9, 82, 10]
[38] [27, 43] [3, 9] [82, 10]
[38] [27] [43] [3] [9] [82] [10]

Merge Phase:
[27, 38] [43] [3, 9] [10, 82]
[27, 38, 43] [3, 9, 10, 82]
[3, 9, 10, 27, 38, 43, 82]


