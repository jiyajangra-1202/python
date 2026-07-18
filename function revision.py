# def greet():
#     print("hello, everyone.I AM JIYA")
# greet()    #print hello
# #block of reusable code that performs a specific task.
# #USE OF FUNCTION:-
# # Avoid repeating code 
# # make program shorter
# #easy to understand,easy to debug and reusable of code
# #TYPES OF FUNCTION:-
# #1.Built-in function:python already provides these.
# print("hello")
# x=len("python")
# print(x)
# print(max(10,20,30))
# #2.User-defined functions(created using def)
# def hello():
#     print("hello everyone")
# hello()    
# ##Function without parameters:-
# def student():
#     print("name:jiya")
#     print("course:python")
# student()    
# ##Function with parameters:-(parameters recieve values)
# def greet(name):
#     print("hello",name)
# greet("jiya")
# greet("subham")    
# ##Function with multiple parameters
# def add(a,b):
#     print(a+b)
# add(5,4)    
# ##Function returning value
# def square(n):
#     return n*n
# x=square(5)
# print(x)
# ##Difference between print() and return
# def add(a,b):
#     print(a+b)
# add(5,4)#using print(cannot store the result)
# def add(a,b):
#     return a+b
# result=add(7,6)
# print(result)#using return 
# ##Default Arguments:-
# def greet(name="student"):
#     print("hello",name)
# greet()
# greet("jiya")      
# ##Keyword Argument:-
# def student(name,age):
#     print(name)
#     print(age)
# student(age=19,name="jiya")     
# ##Positional Arguments:-
# def add(a,b):
#     print(a+b)
# add(10,30)
# ##Variable length arguments(*args)-accepts many values.
# def total(*numbers):
#     print(sum(numbers))
# total(10,20,30)
# ##Keyword variable arguments(**kwargs)
# def details(**data):
#     print(data)
# details(name="jiya",age=19)
# ##Local variable:-exits only inside function.
# def test():
#     x=100
#     print(x)
# test()
# ##Global variable:-
# x=100
# def test():
#     print(x)
# test()
# ##Anonymous function(Lambda)
# square=lambda x:x*x
# print(square(6))            
# ##Recursive Function:-a function calling itself
# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))##Factorial
# ##Function inside function
# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()
# ##Pass statement
# def future():
#     pass#useful when you want to write the function later.
# ##Docstring(explains a function)
# def add(a,b):
#     """Returns sum of two numbers"""
#     return a+b
# print(add.__doc__)
# ##Scope of Variable
# x=78
# def test():
#     x=100
#     print(x)
# test()
# print(x)

# ##PRACTICAL PROGRAM
# ##even or odd
# def evenOdd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# evenOdd(15)  
# ##largest number
# def largest(a,b):
#     if a>b:
#         return a 
#     return b
# print(largest(20,45))    
# ##Prime number
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         return True
#     print(prime(13))
# ##Fibonacci Series
# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fibonacci(10)      
# ##Table
# def table(n):
#     for i in range(1,11):
#         print(n,"x",i,"=",n*i)
# table(5)   
# ##Sum of number
# def total(n):
#     s=0
#     for i in range(1,n+1):
#         s+=i
#         return s
# print(total(10)) 
# ##Palindrome
# def palindrome(text):
#     if text==text[::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome") 
# palindrome("madam")  
# ##Reverse String
# def reverse(text):
#     return text[::-1]
# print(reverse("python"))
# ##Count Vowels
# def vowels(text):
#     count=0
#     for i in text.lower():
#         if i in "aeiou":
#             count+=1
#             return count
# print(vowels("programming"))       
# ##Practice questions:-
# def name():
#     print("jiya")
# name()           #print your name
# def add(a,b):
#     return a+b
# result=add(10,20)
# print("sum=",result)#add two numbers

# ###Practice question:-
# # def calculate(a,b=3,c=4):
# #     return a*b-c
# # print(calculate(5,c=2))

# ##Variable-length arguments:-
# #Someetimes we do not know how many arguments will be passed to a function.
# # in such cases we use *ar/gs//
# #*args stores multiple positional arguments to a tuple
# def add_numbers(*numbers):
#     total=0
#     for num in numbers:
#         total +=num
#         return total
# print(add_numbers(10,20))
# print(add_numbers(5,10,15,20))    
# ##Another example:-
# def show_names(*names):
#     for name in names:
#         print(name)
# show_names("jiya","moni","mahak")        
# #you can combine regular parameters with *args.
# def student(grreeting,*numbers):
#     for name in numbers:
#         print(numbers)
# student(10,20,30,40,50)   
# ##Keyword argument in variable-length:-
# ##it can stores data in dictionary.
# def show_details(**details):
#     for key,value in details.items():
#         print(key,":",value)
# show_details(name="rohit",age=15,city="pune")  
# print(type(show_details))      
# # another examples:-
# def create_profile(**user):
#     print("user profile")
#     print("name:",user.get("name"))
#     print("age:",user.get("age"))
#     print("email:",user.get("email"))
# create_profile(name="sneha",age=25,email="sneha@example.com")    
# ###Local and global variables
# # variables create inside function are called local variable.
# language="python"
# def my_function():
#  print("language:",language)
# print(language)
# ##Example:-
# count=0
# def increase():
#     global count
#     count +=1
# increase()
# increase()
# print(count)

# ##Function documentation:Docstrings
# #it is a short description of what a function does.
# #it is written inside a triple quotes
# def square(number):
#     """
#     this function return the square of a number
#     """
#     return number*number
# print(square(5))
# print(square.__doc__)
# #it is useful for explaining your code.
# ##Type hints in functions:-it show types of data a function expects  and returns.
# #example:-
# def add(a:int,b:int) ->int:
#     return a+b
# print(add(10,20))
# #it do not force the type at runtime, but they make code easier to understand
# ##LAMBDA FUNCTION:-it is a small anonymous function.
# #it is usually used for short operations.
# ##Example:-
# # lambda arguments:expression (syntax)
# square=lambda x:x*x
# print(square(5))
# ##Another examples:-
# add=lambda a,b:a+b
# print(add(7,8))
# #these are commonly used with function like map(),filter(),sorted()
# ##Using Function with lists.
# marks=[10,440,67,87]
# def largest(numbers):
#     largest=numbers[0]
#     for number in numbers:
#         if number>largest:
#             largest=number
#         # return largest
# marks=[10,440,67,87]    
# print(largest(marks))
# ##Function calling other functions
# #this helps divide a big problem into smaller parts
# #example:
# def get_square(number):
#     return number*number
# def print_square(number):
#     result=get_square(number)
#     print("square:",result)

# print_square(8)    

# ##Nested function
# # example:-
# def outer_function():
#     print("this is outer function")

# ##Recursion:-it means a function call itself
# #a base condition to stop recursive.
# #base case= a condition that stops the recursion
# #recursive case= the function calling itself with a modified arguments
# #without a base case, 
# def factorial(n):
#     if n==0 :
#      return 1
#     else:
#      return n * factorial(n-1)
# print(factorial(6))

#######PRACTICE QUESTIONS:-
def calculate(a,b=5):
    return a+b,a*b
x,y=calculate(4)
print(x,y)
print(calculate(4,2)[1])
##2.
def display(a,b,c=10):
    print(a,b,c)
display(1,c=3,b=2)
display(4,5) 
##3.
def calculate(number):
    if number%2==0:
        return number//2
    print("odd number")
    return number*3
print(calculate(8))   
print(calculate(5))   
# ##4.
def add_item(item,container=[]):
    container.append(item)
    return container
print(add_item(1))
print(add_item(2))
print(add_item(3,[]))
print(add_item(4))
# ##5.
# def analyse(first,*values):
#     return first,max(values),sum(values[::2])
# print(analyse(10,3,8,5,2))
# ##6.
def build_record(**data):
    data["total"]=sum(
        value
        for value in data.values()
        if isinstance(value,int)
    )
    return sorted(data.items())
print(build_record(a=2,b=3,name="X"))
# ##7.
# def calculate(a, b, c):  
#        return a + b * c
# values = (2, 3)
# options = {"c": 4}  
# print(calculate(*values, **options)) 
# ##8.
def report(name, *, score=0, passed=True):     
    return f"{name}:{score}:{passed}"  
print(report("Riya", score=88))
print(report("Kabir", passed=False, score=40)) 
# ##9.
def change(number):   
     number += 10    
     return number 
value = 5  
print(change(value), value)  
##10.
def update(data):    
     data[0] += 5  
     data.append(sum(data))  
numbers = [1, 2, 3] 
update(numbers) 
print(numbers) 
# ##11.
# def update(data):
#          data = data + [4]   
#          data[0] = 99   
#          return data 
# numbers = [1, 2, 3]
# new_numbers = update(numbers)
# print(numbers) 
# print(new_numbers) 
# ##12.
def update(record):    
     record["b"] = record.get("b", 0) + 2   
     record = {"c": 3}    
     return record 
data = {"a": 1, "b": 4} 
result = update(data) 
print(data) 
print(result) 
# # Question 13
# def modify(data):   
#       data[1].append(30)    
#       return data + ("done",)
# values = (10, [20])
# result = modify(values) 
# print(values) 
# print(result) 
# ##14.
# x = 10 
# def outer():    
#  x = 20     
#  def inner():      
#        global x    
#        x += 5      
#        print(x)    
#        inner()     
#        print(x) 
#        outer()
#        print(x)  
# #Question 15
# def outer():   
#       number = 1   
#       def inner(): 
#                 nonlocal number    
#                 number *= 3       
#                 return number   
# print(inner(), inner())  
# outer() 
# #16.
# def create_power(exponent):  
#        def calculate(number):       
#           return number ** exponent 
#           return calculate 
# square = create_power(2) 
# cube = create_power(3)
# print(square(4) + cube(2))  
# #Question 17
# functions = [] 
# for number in range(3):  
#  functions.append(lambda: number) 
# print([function() for function in functions]) 
# #Question 18 
# functions = []  
# for number in range(3):     
#    functions.append(lambda number=number: number) 
# print([function() for function in functions])
# #Question 19 
# def apply(function, values): 
#         return [         function(value)       
                                                   
#     for value in values  
                                                            
                                                            
#     if function(value) > 5     ]
# def transform(number):  
#      return number * number - 1  
# print(apply(transform, [1, 2, 3, 4]))
#question20.
numbers = [1, 2, 3, 4, 5] 
result = list(     map(         lambda number: number * 2,       
                         filter(lambda number: number % 2 == 1, numbers)     ) ) 
print(result) 
#ques21.
def add(a, b):    
     return a + b 
def multiply(a, b):  
     return a * b
operations = {     "addition": add,     "multiplication": multiply }  
result = (     operations["addition"](2, 3)     + operations["multiplication"](2, 3) )  
print(result) 
##e.Recursive 
#ques22.
def calculate(number): 
        if number <= 1:   
                  return 1   
        return number + calculate(number - 2) 
print(calculate(6))
##ques23.
def trace(number):  
       if number == 0:  
        return   
       print(number, end=" ")   
       trace(number - 1)   
       print(number, end=" ")  
               
trace(3)
##ques24.
def flatten(data):  
       result = []     
       for item in data:     
            if isinstance(item, list):         
                    result.extend(flatten(item))       
            else:           
                    result.append(item)  
                    return 
            result  
values = [1, [2, [3, 4]], 5] 
print(flatten(values))
#F.Generators and Decorators:-
##ques25.
def sequence(number): 
        while number > 0:    
                 yield number       
                 number -= 2  
                 result = sequence(5)
                 print(next(result)) 
                 print(list(result)) 
##ques26.
def increase(function):   
      def wrapper(number):        
       return function(number) + 1     
      return wrapper 
@increase 
def square(number):
         return number * number 
print(square(4))
##ques27.
def double(function):
         def wrapper(number):        
             return 2 * function(number)    
         return wrapper  
def add_one(function):    
    def wrapper(number):    
     return function(number) + 1    
    return wrapper 
@double 
@add_one
def calculate(number): 
    return number  
print(calculate(5)) 
##Advanced behaviour
##ques28.
def combine(a: int, b: int) -> int:   
      return str(a) + str(b)  
result = combine(2, 3) 
print(result)
print(type(result).__name__)
##ques29.
x = 10 
def display():        
    x = 20 
    print(x) 
    display()
##ques30.
def modify(values):   
     for index, value in enumerate(values):   
              if value % 2 == 0:       
                      values[index] = value // 2      
              else:          
                      values[index] = value * 3 + 1    
                      return tuple(reversed(values)) 
numbers = [1, 2, 3, 4]
result = modify(numbers)  
print(numbers) 
print(result) 
