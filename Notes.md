# **Operators:**
## Difference between `is` and `==`. 
|**S.No**|**`is`**|**`==`**|
|--------|--------|--------|
|**1.**|`is` is a identity operator.|`==` is a relational operator.|
|**2.**|`is` compares the memory address of the two operands. | `==` compares the value of the two operands.|
|**3.**|For Example `a is b`|For Example `a == b`|

# **OOPS:**
## General Parameters:
### self:
&nbsp; self is a parameter of class which points the memory address of the object created for the specific class. self is a mandatory parameter for the object attribute and instance method. 

### cls:
&nbsp; cls is a parameter which points the memory address of the class where we can create object for that class. cls is a mandatory parameter for the class attribute and the class method. 

### Difference between `self` and `cls`:
|**S.No**|**self**|**cls**|
|--------|--------|-------|
|**1.**|self is a parameter which points the memory address of the object.|cls is a parameter which points the memory address of the class.|
|**2.**|Attribute in a self changes object to object of the same class.|Attribute in cls will not change according to object to object in same class.|
|**3.**|self is mandatory parameter for instance attribute and method.|cls is mandatory parameter for the class attribute and method.|