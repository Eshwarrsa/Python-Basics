"""
### Problem: Fibonacci Sequence (Using Recursion)  

Write a program to calculate the `n`th Fibonacci number using recursion.  
The Fibonacci sequence is defined as:  
- **Fib(0) = 0**, **Fib(1) = 1**  
- **Fib(n) = Fib(n-1) + Fib(n-2)** for **n > 1**

#### Example:
- **Input:** `n = 6`
- **Output:** `8`  
(*Explanation:* `0, 1, 1, 2, 3, 5, 8`)
"""

def nth_fibinacci_series(num, a = 0, b = 1):
    if num < 0:
        raise ValueError("Enter positive Number")
    if num == 0:
        return a
    return nth_fibinacci_series(num - 1, b, a + b)

print(nth_fibinacci_series(6))