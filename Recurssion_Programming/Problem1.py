"""
**Write a Python function to find the factorial of a number using recursion.**

For example:  
Input: `5`  
Output: `120`
"""
def factorial(number):
    if number < 0:
        raise ValueError ("For factorial negative and non integer number is not allowed")
    if not isinstance(number, int):
        raise ValueError ("For factorial negative and non integer number is not allowed")
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

number = 0
print(factorial(number))