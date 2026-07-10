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

#####LIST IN PYTHON(USED TO STORE MULTIPLE VALUES IN A SINGLE VARIABLES)
#IT IS ORDERED
#IT IS MUTABLE
#IT ALLOWS DUPLLICATE VALUES
#ELEMENTS ARE ACCESSED USING INDEXED
#CANN STORED DIFFERENT DATA TYPES TOGETHER
a=[]
print(a)#empty list
numbers=[10,20,30,40]
print(numbers)#list with values
data=[10,"python",10.2,True]
print(data)#mixed data types
#ACCESSING LIST ELEMENTS:-
fruits=["apple","mango","banana","cherry","lichi","watermelon"]
print(fruits[0])#positive indexing
print(fruits[-5])#negative indexing
print(fruits[1:5])#list slicing
#modifying a list:-
fruits[1]="orange"
print(fruits)
##list operators:-
a=[1,2]
b=[3,4]
print(a+b)#concatenation
print([1,2]*5)#repetition
##membership operators:-
numbers=[10,20,30]
print(20 in numbers)
print(50 not in numbers)
##LOOPING THROUGH A LIST
fruits=["apple","mango","banana","cherry","lichi","watermelon"]
for fruit in fruits:
    print(fruit)

###important list methods:-
# 1.append(adds one elements at the end)
fruits=["apple","mango","grapes"]
print(fruits.append("orange"))
# 2.extend(adds multiple elements from another iterable)
num=[1,2,3]
print(num.extend([3,4,5]))
# 3.insert(adds an element at a specific index)
print(num.insert(1,7))
#4.remove(removes the first occurences of a value)
num.remove(2)
print(num)
#5.pop(removes and returns an element)
num.pop()
print(num)
#6.clear(removes all elements)
num.clear()
print(num)
#7.index(returns the index of value)
num=[10,20,30]
print(num.index(20))
#8.count(how many times a value appears)
num=[1,2,3,4,2,2,1,3]
num.count(2)
print(num)
#9sort(list in ascending order)
num.sort()
print(num)
#DESCENDING ORDER()
num.sort(reverse=True)
# 10.reverse(reverses the list)
num.reverse()
print(num)
#11.copy(create a shallow copy)
a=[1,2,3]
b=a.copy()
print(b)
###BUILT-IN FUNCTION:-
nums=[1,2,3,4,5]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
##NESTED LISTS:-
matrix=[
    [1,2],
    [3,4],
    [5,6]
]
print(matrix)

####TUPLE IN PYTHON:-
#MULTIPLE VALUES IN A SINGLE VARIABLE.
#ORDERED
# IMMUTABLE
# ALLOWS DUPLICATE VALUES
# SUPPORTS DIFFERENT DATA TYPES
# ENCLOSES IN PARENTTHESES
t=()
print(t)#empty tuples
num=(1,2,3)
print(num)#tuple with values
#Tuple operators:-
# 1.Concatenatiion
a=(1,2)
b=(3,4)
print(a+b)
#2.repetition
print((1,2)*3)
##Important tuple methods:-
num=(1,2,2,3,3,1,4,3)
print(num.count(2))#count()
num=(1,2,2,3,4)
m=num.index(2)
m1=num.index(2,m+1)
print(m1)#indexing

###Packing and Unpacking
student=("jiya",18,"BCA")#tuple packing
name,age,course=student
print(name)
print(age)
print(course)
##Nested tuples
matrix=(
    (1,2),
    (3,4)
)
print(matrix[1][0])

##Converting between list and tuple
#tuple to list
t=(1,2,3)
a=list(t)
print(a)
#list to tuple
a=[1,2,3,4]
b=tuple(a)
print(b)

##deletin a tuple
a=(1,2,3)
del a

####SET IN PYTHON
#unordered
#mutable
# does not allow duplicate values
#unindexed
#enclosed in curly braces{}
#contains different immutable data types
s=set()
print(type(s))
##Adding elements:-
num={1,2,3}
num.add(4)
print(num)#add one element
num.update([4,5,6])
print(num)#update(add multiple elements)
##Removing elements:-
num={10,20,30}
num.remove(20)
print(num)#removes a specific elements
num.discard(100)
print(num)#no error occurs if the element is absent
num.pop()
print(num)#removes and returns a random elements
num.clear()
print(num)#removes all elements
a={1,2,3,4}
b=a.copy()
print(b)#copying a set

###SET OPERATIONS:-
A={1,2,3}
B={3,4,5}
print(A.union(B))#COMBINE ALL UNIQUE ELEMENTS(|)
print(A.intersection(B))#common elements(&)
print(A.difference(B))#elements in the first set but not the second(-)
print(A^B)#Symmetric difference(elemments present in either set but not both)

##Comparison methods
# 1.issubset(checks if one set is completely inside another)
A={1,2}
B={1,2,3}
print(A.issubset(B))
#2.issuperset(checks if a set contains all elemennts of another)
A={1,2,3}
B={1,2}
print(A.issuperset(B))
#3.isdisjoint(checkss whether two sets have no common elements)
print(A.isdisjoint(B))
##Frozen set(it is an immmutable version of a set)
fs=frozenset([1,2,3])
print(fs)#you cannot ad or remove elemmets from a frozenset.
a=[1,2,3,4]
b=set(a)
print(b)#list convert into set

####Dictionary in python
#in the form of key-value pairs
#a dict stores data using keys instead of indexes.
#ordered
#mutable
#keys are unnique(dupllicate keys are not allowed)
#values can repeat(duplicate values are allowed)
# Indexed by keys(values are accessed using keys,not numeric indexes)
student={
    "name":"Jiya",
    "age":19,
     "course":"BCA"
     }
print(student)
print(student.get("name"))
print(student.get("city"))
###Adding new items
student["city"]="delhi"
print(student)
student["age"]=20
print(student)#updating existing values
#Removing items
#pop(removes an item by key and returns its value)
age=student.pop("age")
print(student)
print(student.popitem())#last inserted key-value pair removes
del student["name"]#deletes a specific key
print(student)
print(student.clear())#removes all items

##IMPORTANT DICT METHODS
student={
    "name":"Jiya",
    "age":19,
     "course":"BCA"
     }

print(student.keys())#returns all keys
print(student.values())#returns all values
print(student.items())#returns all items
student={
    "name":"Jiya",
    "age":19,
     "course":"BCA"
     }

student.update({
    "distict":"mahendergarh",
    "date":10
    })
print(student)#add or update multiple items