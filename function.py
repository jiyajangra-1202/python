#function is a block of code that perform a specific task
#instead of writing the same code
#easier to read
#Example with a function
def greet(name):#function definition
    print("hello",name)
    print("welcome to python:")

greet("mehak")#function call    
greet("jiya")

#rules of function
#must start with a letter
#case sensitive
#def is used to define the function
# ()may contain parameters
# : marks the start of the function body
def say_hello():
    print("hello!")
say_hello()    
#FUNCTION IN PARAMETER AND ARGUMENT:-
#Parameter:a variable listed in the function definition
def addition(a,b):#multiple parameter
    print("sum",a+b)
addition(10,20)#argument
#example
def student_info(name,age,grade):
    print("Name:",name)
    print("Age:",age)
    print("Grade:",grade)

student_info("Ravi",16,"BCA")    
student_info("JIYA",19,"BCA")    
student_info("MAHAK",20,"BCA")    
#example
#return statement(it is used to send a value back from a function )
def add(a,b):
    return a+b
result=add(4,6)
print(result*2)
#a python function can return more than one value.
#example:-
def calculate(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
x,y,z=calculate(10,5)

print("add:",x)
print("sub:",y)
print("mul:",z)

#Default parameter:it have predefined values
# if the user does not pass an argument, the default value is used.
#example:-
def greet(name="guest"):
    print("hello",name)
# greet("suman")
greet()

#another example:-
def calculate_bill(amount,tax_rate=0.05):
    total=amount+amount*tax_rate
    return total
# print(calculate_bill(1000))
print(calculate_bill(1000,0.10))

#keyword arguments:-are passed using parameter names.
#this makes the function call clearer.
def student(name,age,city):
    print("Name:",name)
    print("Age:",age)
    print("City:",city)
student(name="jiya",age=19,city="delhi")    
student(city="mumbai",name="moni",age=21)   #ordered can be changed 
