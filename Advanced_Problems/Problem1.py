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

def longest_sequence_of_consecutive(arr):
    quick_sort(arr, 0, len(arr) - 1)
    dic = {}
    lst = []
    for i in range(len(arr) - 1):
        if arr[i] + 1 == arr[i + 1]:
            lst.append(arr[i])
        else:
            if len(lst) not in dic:
                lst.append(arr[i])
                dic[len(lst)] = lst
            lst = []
    keys = list(dic.keys())
    high = keys[0]
    for i in range(1, len(keys)):
        if keys[i] > high:
            high = keys[i]
    return dic[high]


lst = [100, 4, 200, 1, 3, 2]
print(longest_sequence_of_consecutive(lst))