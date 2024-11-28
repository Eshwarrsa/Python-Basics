"""
**Write a Python function to implement binary search on a sorted list. The function should take a sorted list and a target value as input and return the index of the target value if found, or `-1` if not found.**

For example:  
Input: `arr = [1, 3, 5, 7, 9]`, `target = 5`  
Output: `2`
"""
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        
        if target > arr[mid]:
            low = mid + 1
        
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9]
target = 5
print(binary_search(arr, target))
print(binary_search([], 5))  # Output: -1 (empty array)
print(binary_search([1], 1))  # Output: 0 (single element)
print(binary_search([1, 1, 1, 1, 1], 1))  # Output: Any valid index (e.g., 0)
print(binary_search([1, 2, 3, 4, 5], 6))  # Output: -1 (target not in array)