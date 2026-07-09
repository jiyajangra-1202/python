#revision from variable to loop conditional 
name="jiya"
age=19
height=5.1
status=True
print(name)
print(age)
print(height)
print(status)#different data types
#USES OF VARIABLES:-
#store data,perform calculation,reuse values,make programs easier to read,update values easily
#RULES OF VARIABLES:-
#can contain letters,digits or underscores.
#cannot start with a digit.
#can start with underscore
#no spaces,no special characters,cannot used python keywords.
#case sensitive
#ASSIGNING VALUES:-
x=10
print(x)#single assignment
x,y,z=10,20,30
print(x)
print(y)
print(z)#multiple assignment
a=b=c=100
print(a)
print(b)
print(c)#same values to multiple variables
#changing variable values
score=50
print(score)
score=80
print(score)
#DYNAMIC TYPING(it doesnot require declaring the data types)
x=10
print(x)
x="hello"
print(x)
x=5.5
print(x)
#TYPE CHECKING
a=10
b=3.14
c="python"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#input using variables
# name=input("enter your name:")
# print(name)
# age=input("enter your age:")
# print(age)
#Arithmetic with variables:-
a=20
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#Swapping Variables
a=10
b=20
a,b=b,a
print(a)
print(b)
#Using temporary variable
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
#VARIABLE SCOPE
def show():
    x=100
    print(x)
show()#LOCAL VARIABLE(declared inside a function)
x=100
def show():
    print(x)
show()#GLOBAL VARIABLE(declared outside a function)
#Deleting a Variable
x=330
y=200
del x     
print(y)
#PRACTICE PROGRAM:-
Name="jiya"
age=19
print("name",Name)
print("Age",age)#store andd print
#Adding two number
a=100
b=200
print(a+b)
#3.Calculate area of rectangle
Length=43
Breadth=33
area=Length*Breadth
print(area)
#4.Swap two numbers
x=100
y=700
x,y=y,x
print(x)
print(y)
#5.take your input
name=input("enter your name:")
print("welcome!",name)

###DATA TYPES IN PYTHON:-
#stores data efficiently
#perform the correct operations
#prevent invalid operations
#manage memory properly
#Display different data types
a=12
b=12.3
c="python"
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#TYPE CONVERSION:-
num=123
print(float(num)+78)

####STRING IN PYTHON
#SEQUENCE OF CHARACTERSS
# ENCLOSED IN SINGLE,DOUBLE AND TRIPLE QUOTES
# it contain letters,numbers,spaces,symbols,special characters
name="subham"
city='rudrol'
message="python is easy to learn"
print(name[1:3])
print(city[-5:-2])#negative index
#Characteristics:-
# ordered,immutable,supports indexing and slicing
# allows duplicate characters
#String concatenation
first="hello"
second="world"
print(first+""+second)
print("python"*3)#repetition
text="python language"
print("pyt"in text)
print("jav" in text)
print("jav" not in text)#finding values
print(len(text))#length
##IMPORTANT STRING METHODS:-
print(text.upper())#text are in large letter
print(text.lower())#text in smaller letter
print(text.capitalize())#first letter is large
print(text.title())#first character of each letter is capital
print(text.swapcase())#character is swap 
print(text.strip())#remove spaces from both ends
print(text.replace("python","java"))#replace the letter
print(text.find("th"))#returns the first index of a substring
print(text.index("h"))#similar to find but raises the error if the substring is not found
print(text.count("o"))#count occurences
print(text.startswith("py"))#true or false
print(text.endswith("ge"))#true or false
text="python language"
print(text.split())#convert a string into a list
text=["python","language"]
print(" ,".join("text"))#join elements of a list into a string
text="python"
print(text.center(20,"*"))#element in center