# **Basic Topics:**
# Features of Python:
## Dynamic Typing:
&nbsp; &nbsp; We all know that python is dynamically typed programming language. The dynamically typed programming language will analyze the data type of the given variable during the runtime. So, that the same identifier can store different data type. Which you can see in the below example. 
```py
x = 10
x = "hello"
```
while in the strictly typed programming language the data type of that identifier should be declared before that is declared which cannot be used for other datatype. 
```java
int x = 1;
x = 1.1; //Compile Time Error
double x = 1 // Compile time Error
```
The major drawbacks of the dynamic typed language are it takes more time than the strictly typed programming language because while runtime the datatype will be check for each time which takes more time. When ever the user pass inputs the developer can except any type of data type which the developer should handle every possibilites and through checking is necessary is required. It loses the natural compile time polymorphism which will not allows us to write method or function name with same identifier but different data type. 

# Copy:
## Difference between shallow copy and deep copy:
|**S.No**|**Shallow Copy**|**Deep Copy**|
|--------|----------------|-------------|
|**1.**|The process of copying seperate object for the outer object and the inner object points the same reference is known as shallow copy|The process of copying the outer object and inner objects and storing them with different reference is known as deep copy.|
|**2.**|Altering the duplicate inner object will also alter the orginal inner object also.|Altering duplicate inner object will not affect the ordinal inner object.|
|**3.**|The shollow copy can be achived either by slicing or copy function in copy library.|The deep copy can be achived by deepcopy() in copy library. 

## Example:
```py
import copy
a1 = [1, 2, [1, 2, 3], 4]
a2 = [1, 2, [1, 2, 3], 4]
b = copy.copy(a1)
c = copy.deepcopy(a2)
b[2][1] = 99
c[2][1] = 99
```