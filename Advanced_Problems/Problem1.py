"""
**Write a Python function that takes a list of integers and returns the longest sequence of consecutive numbers.**

For example:
- Input: `[100, 4, 200, 1, 3, 2]`
- Output: `[1, 2, 3, 4]`
"""
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    s, e = start, end
    pivot = arr[(start + end) // 2]
    while s <= e:
        while pivot > arr[s]:
            s += 1
        
        while pivot < arr[e]:
            e -= 1
        
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    
    quick_sort(arr, start, e)
    quick_sort(arr, s, end)



lst = [100, 4, 200, 1, 3, 2]