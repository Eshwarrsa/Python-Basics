"""
**Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward. Ignore spaces and case.**

For example:  
Input: `"A man a plan a canal Panama"`  
Output: `True`
"""
def palindrome(word):
    word = "".join((word.lower()).split())
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

word = "A man a plan a canal Panama"
print("Palindrome" if palindrome(word) else "Not a Palindrome")