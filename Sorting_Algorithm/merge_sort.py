"""
Here’s your next **problem** question:

**Write a Python function to sort a list of integers using the merge sort algorithm. The function should take an unsorted list as input and return the sorted list.** 

For example:  
- Input: `[38, 27, 43, 3, 9, 82, 10]`  
- Output: `[3, 9, 10, 27, 38, 43, 82]` 
"""

def sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = sort(left)
    right = sort(right)
    return merge(left, right, arr)
    

def merge(left, right, arr):
    l, r, i = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1
    
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    
    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1
    return arr

lst = [38, 27, 43, 3, 9, 82, 10]
print(len(lst))
print(lst)
sort(lst)
print(lst)