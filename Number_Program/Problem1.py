"""
### Problem: Sum of Digits in a Number  

Write a program to compute the sum of digits of a given integer number.  
If the input is negative, consider only the absolute value of the number.

#### Example:
- **Input:** `n = -123`
- **Output:** `6`  
"""
def sum_of_the_digits(number):
    # Condition to check the number is integer or not
    if not isinstance(number, int):
        raise ValueError("Not a integer")
    
    # Condition to check the number is negative or not
    if (number < 0):
        number = abs(number) # If negative the number is changed to positive
    
    # Loop to add single number
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    
    return res # Return type is integer

print(sum_of_the_digits(-123))