""" 
**Write a Python program to print the following pattern for a given `n`:**  
For example, if `n = 5`:  
```
*
**
***
****
*****
```  
"""

number = int(input("Enter the Number : "))

for line in range(1, number + 1):
    for column in range(line):
        print("*", end = "")
    print()