numbers=[10,20,30,40]
names=["jiya","mahak","moni"]
mixed=[10,"python",5.2,True]
print(numbers,names,mixed)#creating a list
print(len(mixed))
#list is an ordered collection of items.

# Ordered ✅
# Mutable (can be changed) ✅
# Allows duplicate values ✅
# Can store different data types ✅
# Syntax
my_list = [10, 20, 30]

# Example

numbers = [10, 20, 30, 40]

print(numbers)

# Output

[10, 20, 30, 40]
# List Characteristics
data = [1, "Python", 5.6, True]

# Lists can contain

# integers
# float
# strings
# booleans
# other lists
# Accessing Elements
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])

# Output

# Apple

# Negative Index

print(fruits[-1])

# Output

# Orange
# Slicing
nums = [1,2,3,4,5,6]

print(nums[1:4])

# Output

# [2,3,4]

# Examples

nums[:3]

nums[2:]

nums[::-1]
# Modifying List
fruits = ["Apple","Banana"]

fruits[0] = "Mango"

print(fruits)

# Output

# ['Mango', 'Banana']
# Adding Elements

# append()

numbers = [1,2]

numbers.append(3)

# Result

# [1,2,3]

# insert()

numbers.insert(1,100)

# Result

# [1,100,2]

# extend()

a = [1,2]
b = [3,4]

a.extend(b)

# Result

# [1,2,3,4]
# Removing Elements
numbers.remove(2)

# Removes first occurrence.

numbers.pop()

# Removes last item.

numbers.pop(1)

# Removes item at index 1.

numbers.clear()

# Removes everything.

# Useful Functions
len(list)

max(list)

min(list)

sum(list)

sorted(list)

list.reverse()

list.sort()

# Example

numbers=[4,1,8,2]

numbers.sort()

print(numbers)

# Output

# [1,2,4,8]
# List Comprehension

# Normal

squares=[]

for i in range(5):
    squares.append(i*i)

# Using List Comprehension

squares=[i*i for i in range(5)]

# Output

# [0,1,4,9,16]
# Nested List
matrix = [
    [1,2],
    [3,4]
]

print(matrix[1][0])

# Output

# 3
# Common List Methods
# Method	Description
# append()	Add at end
# extend()	Add multiple items
# insert()	Add at index
# remove()	Remove by value
# pop()	Remove by index
# clear()	Remove all
# sort()	Sort list
# reverse()	Reverse
# copy()	Copy list
# count()	Count occurrences
# index()	Find position
# Practice Questions (List)
# Basic
# Create a list of 5 fruits.
# Print the third element.
# Change the first element.
# Add a new fruit.
# Remove a fruit.
# Intermediate
# Find largest number.
# Reverse a list.
# Remove duplicates.
# Find second largest number.
# Merge two lists.
# Advanced
# Rotate list left by k positions.
# Find frequency of each element.
# Flatten nested list.
# Find missing number.
# Implement bubble sort without using sort().
# 2. TUPLE
# What is Tuple?

# Tuple is an ordered collection.

# Ordered ✅
# Immutable ✅
# Allows duplicates ✅

# Syntax

t = (10,20,30)
# Access
t=(1,2,3)

print(t[1])

# Output

# 2
# Cannot Modify
t[0]=100

# Output

# TypeError
# Tuple Packing
person = ("John",25,"USA")
# Tuple Unpacking
name,age,country = person

print(name)
# Single Element Tuple

# Wrong

a=(5)

# Correct

a=(5,)
# Tuple Methods
# count()

# index()

# Example

t=(1,2,2,3)

print(t.count(2))

# Output

# 2
# Why Tuple?
# Faster than list
# Safe data
# Dictionary keys
# Return multiple values
# Practice Questions (Tuple)

# Basic

# Create tuple of 5 numbers.
# Access last element.
# Count occurrences.

# Intermediate

# Convert tuple to list.
# Find maximum value.
# Reverse tuple.

# Advanced

# Swap variables using tuple.
# Nested tuple operations.
# Tuple unpacking with *.

# Example

a,b,*c=(1,2,3,4,5)

print(c)

# Output

# [3,4,5]
# 3. DICTIONARY
# What is Dictionary?

# Dictionary stores data in

# Key : Value

# Properties

# Ordered (Python 3.7+) ✅
# Mutable ✅
# No duplicate keys ✅

# Syntax

student={
    "name":"Rahul",
    "age":21
}
# Access Value
print(student["name"])

# Using get()

student.get("age")
# Add New Key
student["city"]="Delhi"
# Update
student["age"]=22
# Delete
del student["age"]

# or

student.pop("age")
# Dictionary Methods
# keys()

# values()

# items()

# update()

# clear()

# copy()

# pop()
# Loop Dictionary
for key,value in student.items():
    print(key,value)
# Nested Dictionary
students={
    "A":{
        "Age":20,
        "Marks":80
    }
}

# Access

students["A"]["Marks"]
# Dictionary Comprehension
square={
    x:x*x
    for x in range(5)
}

# Output

# {
# 0:0,
# 1:1,
# 2:4,
# 3:9,
# 4:16
# }
# Practice Questions (Dictionary)

# Basic

# Create student dictionary.
# Print all keys.
# Print all values.
# Update age.
# Delete city.

# Intermediate

# Count frequency of characters.
# Merge dictionaries.
# Sort dictionary by value.

# Advanced

# Invert dictionary.
# Group words by first letter.
# Nested dictionary manipulation.
# Build phone book.
# 4. SET
# What is Set?

# Set is an unordered collection.

# Properties

# Unordered ✅
# Mutable ✅
# No duplicates ✅

# Syntax

numbers={1,2,3}

# Duplicates Automatically Removed

a={1,2,2,3}

print(a)

# Output

# {1,2,3}
# Add Element
numbers.add(10)
# Remove
numbers.remove(2)

# If absent

# KeyError

# Safer

numbers.discard(2)
# Set Operations

# Union

A={1,2,3}
B={3,4,5}

print(A|B)

# Output

# {1,2,3,4,5}

# Intersection

# A&B

# Output

# {3}

# Difference

# A-B

# Output

# {1,2}

# Symmetric Difference

# A^B

# Output

# {1,2,4,5}
# Set Methods
# add()

# remove()

# discard()

# clear()

# copy()

# union()

# intersection()

# difference()

# issubset()

# issuperset()
# Frozen Set

# Immutable set

fs=frozenset([1,2,3])

# Cannot modify.

# Practice Questions (Set)

# Basic

# Create set.
# Add element.
# Remove element.
# Find length.
# Check membership.

# Intermediate

# Union.
# Intersection.
# Difference.
# Remove duplicates from list.

# Advanced

# Find common words between two sentences.
# Check subset.
# Find unique characters in string.
# Implement recommendation system using set intersections.
# Comparison Table
# Feature	List	Tuple	Dictionary	Set
# Ordered	✅	✅	✅ (3.7+)	❌
# Mutable	✅	❌	✅	✅
# Duplicate Values	✅	✅	Keys ❌, Values ✅	❌
# Indexing	✅	✅	❌ (use keys)	❌
# Key-Value	❌	❌	✅	❌
# Fast Membership (in)	Medium	Medium	Fast	Fast
# Typical Use	General collection	Fixed data	Mappings	Unique items
# When to Use What?
# Use a list when you need an ordered collection that you will modify frequently (e.g., a shopping cart or a list of tasks).
# Use a tuple when the data should not change (e.g., geographic coordinates or RGB color values).
# Use a dictionary when you need to associate keys with values (e.g., student records, configuration settings).
# Use a set when uniqueness matters or you need fast membership tests and set operations (e.g., removing duplicates or comparing groups).
# Complete Practice Roadmap (50 Questions)
# Beginner (1–10)
# Create a list of numbers.
# Find the length of a list.
# Append an element.
# Remove an element.
# Create a tuple.
# Access tuple elements.
# Create a dictionary.
# Print dictionary keys.
# Create a set.
# Remove duplicates from a list using a set.
# Easy (11–20)
# Find the largest element in a list.
# Find the smallest element in a tuple.
# Count occurrences of an item in a list.
# Reverse a list.
# Merge two dictionaries.
# Check if a key exists in a dictionary.
# Compute the union of two sets.
# Compute the intersection of two sets.
# Sort a list in descending order.
# Create a dictionary from two lists (keys and values).
# Intermediate (21–35)
# Find the second largest number in a list.
# Rotate a list by k positions.
# Remove duplicates while preserving order.
# Find the frequency of each element in a list.
# Group words by their first letter using a dictionary.
# Count the frequency of characters in a string.
# Flatten a nested list.
# Transpose a matrix (list of lists).
# Merge nested dictionaries recursively.
# Find common elements among three sets.
# Check if two lists contain the same unique elements.
# Build a phone book using a dictionary.
# Use tuple unpacking with * to capture remaining values.
# Create a multiplication table using a nested list comprehension.
# Find the symmetric difference between two sets.
# Advanced (36–50)
# Implement bubble sort without using sort().
# Implement selection sort.
# Implement insertion sort.
# Rotate a matrix by 90 degrees.
# Solve the Two Sum problem using a dictionary.
# Find the first non-repeating character using a dictionary.
# Find all duplicate elements in a list.
# Build an inventory management system with dictionaries and lists.
# Implement a contact book application (CRUD operations).
# Find the longest consecutive sequence using a set.
# Solve the Group Anagrams problem using a dictionary.
# Implement an LRU cache using a dictionary (or collections.OrderedDict).
# Build a mini library management system using nested dictionaries.
# Create a simple student result management system with dictionaries, lists, and tuples.