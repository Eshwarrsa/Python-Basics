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