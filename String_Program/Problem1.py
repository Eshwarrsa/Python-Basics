"""
**Write a Python function that takes a string as input and returns the string with all the vowels removed.**  

For example:  
Input: `"Hello World"`  
Output: `"Hll Wrld"`
"""
def remove_vowels(word, res = ""):
    res = [char for char in word if char not in "aeiouAEIOU"]
    return "".join(res)

word = "Hello World"
print(remove_vowels(word))