# An array is a data structure used to store multiple values of the same data type in contiguous memory locations. Arrays allow efficient storage and retrieval of elements using an index.

# In many programming languages such as C, C++, and Java, arrays are built-in data structures.

# Example (Concept)
# Index :   0   1   2   3   4

# Array :  10  20  30  40  50
# Arrays in Python

# Python does not have a built-in array type like C or Java for general-purpose programming. Instead, Python uses Lists, which behave like dynamic arrays.

# Python also provides an array module for storing elements of the same type efficiently, but for most programming tasks and introductory courses, lists are used as arrays.

# Example:

# numbers = [10, 20, 30, 40, 50]
# print(numbers)

# Output

# [10, 20, 30, 40, 50]
# 2. Characteristics of Python Lists
# Ordered collection
# Mutable (elements can be changed)
# Dynamic size (can grow or shrink)
# Supports duplicate values
# Supports different data types
# Indexed (starts from 0)
# Allows nested lists
# 3. Advantages of Python Lists
# Easy to create
# Dynamic memory allocation
# Rich built-in methods
# Supports slicing
# Easy insertion and deletion
# Can store different data types
# 4. Limitations
# Slower than arrays for numerical computations
# Consumes more memory
# Insertion at the beginning is costly
# Mixed data types can reduce performance
# 5. Creating a List
# Syntax
# list_name = [element1, element2, element3]
# Example
# marks = [75, 82, 91, 68, 88]
# print(marks)

# Output

# [75, 82, 91, 68, 88]
# 6. Accessing Elements
# Positive Indexing
# fruits = ["Apple", "Banana", "Orange", "Mango"]

# print(fruits[0])
# print(fruits[2])

# Output

# Apple
# Orange
# Negative Indexing
# fruits = ["Apple", "Banana", "Orange", "Mango"]

# print(fruits[-1])
# print(fruits[-2])

# Output

# Mango
# Orange
# 7. List Slicing
# numbers = [10,20,30,40,50,60]

# print(numbers[1:4])

# Output

# [20, 30, 40]
# 8. Updating Elements
# numbers = [10,20,30]

# numbers[1] = 100

# print(numbers)

# Output

# [10, 100, 30]
# 9. Traversing a List
# numbers = [5,10,15,20]

# for item in numbers:
#     print(item)
# 10. Common List Methods
# Method	Description
# append()	Add an element at the end
# insert()	Insert an element at a specific position
# remove()	Remove the first matching element
# pop()	Remove an element by index (or last by default)
# sort()	Sort the list
# reverse()	Reverse the list
# count()	Count occurrences of a value
# index()	Find the index of a value
# extend()	Add another iterable to the list
# clear()	Remove all elements
# copy()	Create a shallow copy
# Programs on Python Arrays (Lists)
# Program 1 – Create a List
# Problem Statement

# Write a Python program to create and display a list.

# Algorithm
# Create a list.
# Print the list.
# Python Code
# numbers = [10, 20, 30, 40, 50]

# print("List:", numbers)
# Output
# List: [10, 20, 30, 40, 50]
# Time Complexity

# O(1) (printing is proportional to output size)

# Space Complexity

# O(n)

# Notes
# Lists are enclosed in square brackets [].
# Elements are separated by commas.
# Program 2 – Print All Elements
# Problem Statement

# Display all elements of a list.

# Algorithm
# Create a list.
# Use a for loop.
# Print each element.
# Python Code
# numbers = [12, 25, 18, 40, 55]

# print("Elements are:")

# for value in numbers:
#     print(value)
# Output
# Elements are:
# 12
# 25
# 18
# 40
# 55
# Time Complexity

# O(n)

# Space Complexity

# O(1)

# Program 3 – Find Length of a List
# Problem Statement

# Find the number of elements in a list.

# Algorithm
# Create a list.
# Use len().
# Display the result.
# Python Code
# numbers = [5, 10, 15, 20, 25]

# length = len(numbers)

# print("Length =", length)
# Output
# Length = 5
# Time Complexity

# O(1)

# Space Complexity

# O(1)

# Program 4 – Find Maximum Element
# Problem Statement

# Find the largest element in a list.

# Algorithm
# Create a list.
# Use max().
# Display the largest value.
# Python Code
# numbers = [12, 67, 45, 89, 23]

# largest = max(numbers)

# print("Largest element =", largest)
# Output
# Largest element = 89
# Time Complexity

# O(n)

# Space Complexity

# O(1)

# Program 5 – Find Minimum Element
# Python Code
# numbers = [12, 67, 45, 89, 23]

# smallest = min(numbers)

# print("Smallest element =", smallest)
# Output
# Smallest element = 12
# Time Complexity

# O(n)

# Program 6 – Sum of List Elements
# Python Code
# numbers = [10, 20, 30, 40, 50]

# total = sum(numbers)

# print("Sum =", total)
# Output
# Sum = 150
# Time Complexity

# O(n)

# Program 7 – Average of List Elements
# Python Code
# numbers = [20, 30, 40, 50]

# average = sum(numbers) / len(numbers)

# print("Average =", average)
# Output
# Average = 35.0
# Time Complexity

# O(n)

# Program 8 – Reverse a List
# Method 1: Using reverse()
# numbers = [10, 20, 30, 40]

# numbers.reverse()

# print(numbers)
# Output
# [40, 30, 20, 10]
# Method 2: Using Slicing
# numbers = [10, 20, 30, 40]

# print(numbers[::-1])
# Output
# [40, 30, 20, 10]
# Program 9 – Sort a List
# Ascending Order
# numbers = [50, 10, 80, 30, 20]

# numbers.sort()

# print(numbers)
# Output
# [10, 20, 30, 50, 80]
# Descending Order
# numbers = [50, 10, 80, 30, 20]

# numbers.sort(reverse=True)

# print(numbers)
# Output
# [80, 50, 30, 20, 10]
# Program 10 – Search an Element
# numbers = [10, 20, 30, 40]

# search = 30

# if search in numbers:
#     print("Element Found")
# else:
#     print("Element Not Found")
# Output
# Element Found
# Program 11 – Insert an Element
# numbers = [10, 20, 40, 50]

# numbers.insert(2, 30)

# print(numbers)
# Output
# [10, 20, 30, 40, 50]
# Program 12 – Delete an Element
# numbers = [10, 20, 30, 40]

# numbers.remove(30)

# print(numbers)
# Output
# [10, 20, 40]
# Program 13 – Merge Two Lists
# list1 = [10, 20, 30]
# list2 = [40, 50, 60]

# merged = list1 + list2

# print(merged)
# Output
# [10, 20, 30, 40, 50, 60]
# Program 14 – Remove Duplicates
# numbers = [10, 20, 20, 30, 40, 40, 50]

# unique = list(set(numbers))

# print(unique)
# Output
# [10, 20, 30, 40, 50]

# Note: Converting to a set removes duplicates but does not preserve the original order.

# Program 15 – Find the Second Largest Element
numbers = [10, 45, 32, 78, 56]

numbers = sorted(set(numbers))

print("Second Largest =", numbers[-2])
Output
Second Largest = 56
Program 16 – Count Frequency of an Element
numbers = [10, 20, 20, 30, 20, 40]

count = numbers.count(20)

print("Frequency =", count)
# Output
# Frequency = 3
# Program 17 – Rotate a List (Left Rotation by One Position)
# numbers = [10, 20, 30, 40, 50]

# rotated = numbers[1:] + numbers[:1]

# print(rotated)
# Output
# [20, 30, 40, 50, 10]
# Program 18 – Copy a List
# original = [10, 20, 30]

# copied = original.copy()

# print("Original:", original)
# print("Copied:", copied)
# Output
# Original: [10, 20, 30]
# Copied: [10, 20, 30]
# Real-Life Applications of Lists
# Student marks management
# Employee records
# Shopping cart items
# Attendance registers
# Inventory management
# Banking transactions
# Contact lists
# Online examination systems
# Common Mistakes
# Using an invalid index (IndexError)
# Modifying a list while iterating over it
# Confusing append() and extend()
# Assuming set() preserves order
# Forgetting that lists are mutable
# Best Practices
# Use meaningful variable names.
# Prefer built-in functions (sum, max, min, len) when appropriate.
# Avoid unnecessary nested loops for large lists.
# Use list comprehensions for concise and readable code where suitable.
# Validate indices before accessing elements.