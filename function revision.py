def greet():
    print("hello, everyone.I AM JIYA")
greet()    #print hello
#block of reusable code that performs a specific task.
#USE OF FUNCTION:-
# Avoid repeating code 
# make program shorter
#easy to understand,easy to debug and reusable of code
#TYPES OF FUNCTION:-
#1.Built-in function:python already provides these.
print("hello")
x=len("python")
print(x)
print(max(10,20,30))
#2.User-defined functions(created using def)
def hello():
    print("hello everyone")
hello()    
##Function without parameters:-
def student():
    print("name:jiya")
    print("course:python")
student()    
##Function with parameters:-(parameters recieve values)
def greet(name):
    print("hello",name)
greet("jiya")
greet("subham")    
##Function with multiple parameters
def add(a,b):
    print(a+b)
add(5,4)    
##Function returning value
def square(n):
    return n*n
x=square(5)
print(x)
##Difference between print() and return
def add(a,b):
    print(a+b)
add(5,4)#using print(cannot store the result)
def add(a,b):
    return a+b
result=add(7,6)
print(result)#using return 
##Default Arguments:-
def greet(name="student"):
    print("hello",name)
greet()
greet("jiya")      
##Keyword Argument:-
def student(name,age):
    print(name)
    print(age)
student(age=19,name="jiya")     
##Positional Arguments:-
def add(a,b):
    print(a+b)
add(10,30)
##Variable length arguments(*args)-accepts many values.
def total(*numbers):
    print(sum(numbers))
total(10,20,30)
##Keyword variable arguments(**kwargs)
def details(**data):
    print(data)
details(name="jiya",age=19)
##Local variable:-exits only inside function.
def test():
    x=100
    print(x)
test()
##Global variable:-
x=100
def test():
    print(x)
test()
##Anonymous function(Lambda)
square=lambda x:x*x
print(square(6))            
##Recursive Function:-a function calling itself
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))##Factorial
##Function inside function
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()
##Pass statement
def future():
    pass#useful when you want to write the function later.
##Docstring(explains a function)
def add(a,b):
    """Returns sum of two numbers"""
    return a+b
print(add.__doc__)
##Scope of Variable
x=78
def test():
    x=100
    print(x)
test()
print(x)

##PRACTICAL PROGRAM
##even or odd
def evenOdd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
evenOdd(15)  
##largest number
def largest(a,b):
    if a>b:
        return a 
    return b
print(largest(20,45))    
##Prime number
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
    print(prime(13))
##Fibonacci Series
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(10)      
##Table
def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
table(5)   
##Sum of number
def total(n):
    s=0
    for i in range(1,n+1):
        s+=i
        return s
print(total(10)) 
##Palindrome
def palindrome(text):
    if text==text[::-1]:
        print("palindrome")
    else:
        print("not palindrome") 
palindrome("madam")  
##Reverse String
def reverse(text):
    return text[::-1]
print(reverse("python"))
##Count Vowels
def vowels(text):
    count=0
    for i in text.lower():
        if i in "aeiou":
            count+=1
            return count
print(vowels("programming"))       
##Practice questions:-
def name():
    print("jiya")
name()           #print your name
def add(a,b):
    return a+b
result=add(10,20)
print("sum=",result)#add two numbers

###Practice question:-
# def calculate(a,b=3,c=4):
#     return a*b-c
# print(calculate(5,c=2))

##Variable-length arguments:-
#Someetimes we do not know how many arguments will be passed to a function.
# in such cases we use *ar/gs//
#*args stores multiple positional arguments to a tuple
def add_numbers(*numbers):
    total=0
    for num in numbers:
        total +=num
        return total
print(add_numbers(10,20))
print(add_numbers(5,10,15,20))    
##Another example:-
def show_names(*names):
    for name in names:
        print(name)
show_names("jiya","moni","mahak")        
#you can combine regular parameters with *args.
def student(grreeting,*numbers):
    for name in numbers:
        print(numbers)
student(10,20,30,40,50)   
##Keyword argument in variable-length:-
##it can stores data in dictionary.
def show_details(**details):
    for key,value in details.items():
        print(key,":",value)
show_details(name="rohit",age=15,city="pune")  
print(type(show_details))      
# another examples:-
def create_profile(**user):
    print("user profile")
    print("name:",user.get("name"))
    print("age:",user.get("age"))
    print("email:",user.get("email"))
create_profile(name="sneha",age=25,email="sneha@example.com")    
###Local and global variables
# variables create inside function are called local variable.
language="python"
def my_function():
 print("language:",language)
print(language)
##Example:-
count=0
def increase():
    global count
    count +=1
increase()
increase()
print(count)

##Function documentation:Docstrings
#it is a short description of what a function does.
#it is written inside a triple quotes
def square(number):
    """
    this function return the square of a number
    """
    return number*number
print(square(5))
print(square.__doc__)
#it is useful for explaining your code.
##Type hints in functions:-it show types of data a function expects  and returns.
#example:-
def add(a:int,b:int) ->int:
    return a+b
print(add(10,20))
#it do not force the type at runtime, but they make code easier to understand
##LAMBDA FUNCTION:-it is a small anonymous function.
#it is usually used for short operations.
##Example:-
# lambda arguments:expression (syntax)
square=lambda x:x*x
print(square(5))
##Another examples:-
add=lambda a,b:a+b
print(add(7,8))
#these are commonly used with function like map(),filter(),sorted()
##Using Function with lists.
marks=[10,440,67,87]
def largest(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
        # return largest
marks=[10,440,67,87]    
print(largest(marks))
##Function calling other functions
#this helps divide a big problem into smaller parts
#example:
def get_square(number):
    return number*number
def print_square(number):
    result=get_square(number)
    print("square:",result)

print_square(8)    

##Nested function
# example:-
def outer_function():
    print("this is outer function")

##Recursion:-it means a function call itself
#a base condition to stop recursive.
#base case= a condition that stops the recursion
#recursive case= the function calling itself with a modified arguments
#without a base case, 
def factorial(n):
    if n==0 :
     return 1
    else:
     return n * factorial(n-1)
print(factorial(6))