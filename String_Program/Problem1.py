"""
### Problem: Reverse a String  

Write a program to reverse a given string without using any built-in reverse functions.  
The program should handle edge cases like empty strings and strings with special characters.  

#### Example:
- **Input:** `"Hello, World!"`
- **Output:** `"!dlroW ,olleH"`
"""
# Function to reverse the string
def reverse(word):
    # Condition to check the type of input
    if not isinstance(word, str):
        raise ValueError("The given data is not string type")
    
    # Condition to check it is empty string or just a character
    if word == "" or len(word) == 1:
        return word
    
    # To reverse the string
    res = ""
    for char in word:
        res = char + res
    
    return res # Return type is string

input = "Hello, World!"
print(reverse(input))