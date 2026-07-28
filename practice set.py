# 1. Basic Python
# Question 1: Print "Hello, Python!"
# print("Hello, Python!")
# print("Welcome to Programming")
# Question 2: Print your Name, Age, and City
# name = "Jiya"
# age = 20
# city = "Delhi"

# print("Name:", name)
# print("Age:", age)
# print("City:", city)
# 2. Variables and Data Types
# Question 3: Store different data types and print their types.
# name = "Rahul"
# age = 21
# height = 5.8
# is_student = True

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))
# Question 4: Take user input and convert it into integer.
# age = input("Enter your age: ")

# print(type(age))

# age = int(age)

# print(type(age))
# 3. Strings
# Question 5: Find the length of a string.
# name = input("Enter your name: ")

# print("Length =", len(name))
# Question 6: Reverse a string.
# text = input("Enter a string: ")

# print(text[::-1])
# Question 7: Count vowels.
# text = input("Enter a string: ")

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print("Total vowels =", count)
# Question 8: Check Palindrome
# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# 4. Lists
# Question 9: Create a list and print elements.
# fruits = ["Apple", "Banana", "Mango", "Orange"]

# print(fruits)
# Question 10: Add and Remove Elements
# fruits = ["Apple", "Banana", "Mango"]

# fruits.append("Grapes")

# fruits.remove("Banana")

# print(fruits)
# Question 11: Find Largest Number
# numbers = [10, 25, 7, 90, 55]

# print("Largest =", max(numbers))
# Question 12: Sort a List
# numbers = [45, 20, 70, 15, 90]

# numbers.sort()

# print(numbers)
# 5. Tuples
# Question 13: Create a Tuple
# numbers = (10, 20, 30, 40, 50)

# print(numbers)
# Question 14: Access Tuple Elements
# numbers = (10, 20, 30, 40)

# print("First =", numbers[0])
# print("Last =", numbers[-1])
# Question 15: Count Occurrence
# numbers = (10, 20, 10, 30, 10)

# print(numbers.count(10))
# 6. Dictionaries
# Question 16: Create Student Dictionary
# student = {
#     "Name": "Rahul",
#     "Age": 20,
#     "Course": "BCA"
# }

# print(student)
# Question 17: Add New Item
# student = {
#     "Name": "Rahul",
#     "Age": 20
# }

# student["City"] = "Delhi"

# print(student)
# Question 18: Update Dictionary
# student = {
#     "Name": "Rahul",
#     "Age": 20
# }

# student["Age"] = 21

# print(student)
# Question 19: Print Keys and Values
# student = {
#     "Name": "Rahul",
#     "Age": 20,
#     "Course": "BCA"
# }

# print(student.keys())

# print(student.values())
# 7. Sets
# Question 20: Create a Set
# numbers = {10, 20, 30, 40}

# print(numbers)
# Question 21: Add and Remove Elements
# numbers = {10, 20, 30}

# numbers.add(40)

# numbers.remove(20)

# print(numbers)
# Question 22: Union of Sets
# A = {1,2,3}

# B = {3,4,5}

# print(A.union(B))
# Question 23: Intersection
# A = {1,2,3}

# B = {2,3,4}

# print(A.intersection(B))
# 8. Conditional Statements
# Question 24: Even or Odd
# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# Question 25: Positive, Negative or Zero
# num = int(input("Enter number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")
# Question 26: Largest of Three Numbers
# a = int(input())
# b = int(input())
# c = int(input())

# if a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)
# Question 27: Grade Calculator
# marks = int(input("Enter Marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Fail")
# 9. Loops
# Question 28: Print Numbers 1 to 10
# for i in range(1,11):
#     print(i)
# Question 29: Multiplication Table
# num = int(input("Enter number: "))

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
# Question 30: Sum of First 100 Numbers
# total = 0

# for i in range(1,101):
#     total += i

# print(total)
# Question 31: Factorial
# num = int(input("Enter number: "))

# fact = 1

# for i in range(1,num+1):
#     fact *= i

# print(fact)
# Question 32: Count Digits
# num = int(input("Enter number: "))

# count = 0

# while num > 0:
#     count += 1
#     num = num // 10

# print(count)
# Question 33: Reverse a Number
# num = int(input("Enter number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)
# Question 34: Print Star Pattern
# for i in range(1,6):
#     print("*" * i)
# 10. Mixed Practice
# Question 35: Remove Duplicates from a List
# numbers = [10,20,30,20,40,10]

# numbers = list(set(numbers))

# print(numbers)
# Question 36: Find Common Elements
# list1 = [1,2,3,4]

# list2 = [3,4,5,6]

# common = set(list1).intersection(set(list2))

# print(common)
# Question 37: Frequency of Characters
# text = input("Enter string: ")

# frequency = {}

# for ch in text:
#     frequency[ch] = frequency.get(ch, 0) + 1

# print(frequency)
# Question 38: Count Uppercase and Lowercase Letters
# text = input("Enter string: ")

# upper = 0
# lower = 0

# for ch in text:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1

# print("Uppercase:", upper)
# print("Lowercase:", lower)

# 1. Introduction to Python

# Python is a high-level, interpreted, object-oriented, general-purpose programming language developed by Guido van Rossum in 1991.

# Python is one of the easiest programming languages to learn because of its simple syntax and readability.

# Where Python is Used
# Artificial Intelligence
# Machine Learning
# Data Science
# Web Development
# Automation
# Cyber Security
# Game Development
# Desktop Applications
# Cloud Computing
# Internet of Things (IoT)
# Features of Python

# ✔ Easy to Learn

# ✔ Open Source

# ✔ Free to Use

# ✔ Platform Independent

# ✔ Object-Oriented

# ✔ Large Standard Library

# ✔ Supports GUI Programming

# ✔ Dynamically Typed

# ✔ Automatic Memory Management

# ✔ Interpreted Language

# Advantages
# Less code
# Easy debugging
# Huge community support
# Cross-platform
# Fast development
# Disadvantages
# Slower than C/C++
# High memory usage
# Not ideal for mobile apps
# Runtime errors due to dynamic typing
# First Python Program
# print("Hello World")

# Output

# Hello World
# Comments

# Single-line comment

# # This is a comment
# print("Python")

# Multi-line comment

# """
# This
# is
# a
# multi-line
# comment
# """
# Variables
# Definition

# A variable is a named memory location used to store data.

# Example

# name = "Rahul"
# age = 20
# marks = 89.5

# Python automatically identifies the data type.

# Rules for Naming Variables

# Allowed

# student_name
# roll_no
# _marks

# Not Allowed

# 1name
# class
# student-name
# Valid Variable Examples
# x = 10

# name = "Amit"

# price = 99.99

# is_pass = True
# Multiple Assignment
# a = b = c = 100

# print(a)
# print(b)
# print(c)

# Output

# 100
# 100
# 100
# Multiple Variables
# name, age, city = "Rahul", 20, "Delhi"

# print(name)
# print(age)
# print(city)
# Swapping Variables

# Without third variable

# a = 10
# b = 20

# a, b = b, a

# print(a)
# print(b)

# Output

# 20
# 10
# Important Points
# Variable names are case-sensitive.
# Use meaningful names.
# Avoid Python keywords.
# Data Types

# Everything in Python is an object.

# Use

# type(variable)

# to know its type.

# Numeric Data Types
# Integer (int)

# Whole numbers.

# x = 100

# print(type(x))

# Output

# <class 'int'>
# Float

# Decimal numbers.

# pi = 3.14

# print(type(pi))

# Output

# <class 'float'>
# Complex
# z = 3 + 5j

# print(type(z))

# Output

# <class 'complex'>
# String

# Collection of characters.

# name = "Python"

# print(name)

# Access characters

# name = "Python"

# print(name[0])
# print(name[3])

# Output

# P
# h

# Negative Indexing

# name = "Python"

# print(name[-1])

# Output

# n

# Slicing

# name = "Programming"

# print(name[0:6])

# Output

# Progra

# Useful String Functions

# text = "python"

# print(text.upper())

# print(text.capitalize())

# print(text.title())

# print(len(text))
# Boolean

# Contains only

# True

# False

# Example

# is_student = True

# print(type(is_student))
# List

# Ordered

# Mutable

# Allows duplicates

# fruits = ["Apple","Banana","Mango"]

# print(fruits)

# Access

# print(fruits[1])

# Modify

# fruits[1] = "Orange"

# Append

# fruits.append("Kiwi")
# Tuple

# Ordered

# Immutable

# numbers = (10,20,30)

# print(numbers)
# Set

# Unordered

# Unique elements

# colors = {"Red","Blue","Green"}

# print(colors)
# Dictionary

# Stores data as key-value pairs.

# student = {

# "name":"Amit",

# "Age":20,

# "Marks":90

# }

# print(student)

# Access

# print(student["Marks"])
# Data Type Comparison
# Data Type	Ordered	Mutable	Duplicate
# List	Yes	Yes	Yes
# Tuple	Yes	No	Yes
# Set	No	Yes	No
# Dictionary	Yes	Yes	Keys No
# Type Conversion

# Implicit

# a = 10

# b = 2.5

# print(a+b)

# Output

# 12.5

# Explicit

# age = "20"

# print(int(age))
# User Input
# name = input("Enter name : ")

# print(name)

# Input Integer

# age = int(input("Enter age : "))

# Input Float

# salary = float(input("Salary : "))
# Operators
# Arithmetic
# a = 10
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# Comparison
# print(10 > 5)

# print(5 == 5)

# print(10 != 20)
# Logical
# print(True and False)

# print(True or False)

# print(not True)
# Assignment
# x = 10

# x += 5

# print(x)
# Membership
# text = "Python"

# print("P" in text)
# Identity
# a = [1,2]

# b = a

# print(a is b)
# Loops

# A loop repeats a block of code multiple times.

# Types

# for loop
# while loop
# For Loop

# Syntax

# for variable in sequence:
#     statement

# Example

# for i in range(5):

#     print(i)

# Output

# 0
# 1
# 2
# 3
# 4

# Range Examples

# range(5)

# range(1,6)

# range(2,20,2)

# Print Even Numbers

# for i in range(2,21,2):

#     print(i)

# Print Table

# num = 7

# for i in range(1,11):

#     print(num*i)

# Sum of First 10 Numbers

# total = 0

# for i in range(1,11):

#     total += i

# print(total)

# Output

# 55
# While Loop

# Syntax

# while condition:

#     statement

# Example

# i = 1

# while i <= 5:

#     print(i)

#     i += 1
# Infinite Loop
# while True:

#     print("Hello")

# Stop using Ctrl + C in the terminal.

# Loop Control Statements
# Break
# for i in range(10):

#     if i == 5:

#         break

#     print(i)
# Continue
# for i in range(6):

#     if i == 3:

#         continue

#     print(i)
# Pass
# for i in range(5):

#     pass
# Nested Loop
# for i in range(1,4):

#     for j in range(1,4):

#         print(i,j)

# Output

# 1 1

# 1 2

# 1 3

# 2 1

# 2 2

# 2 3

# 3 1

# 3 2

# 3 3
# Extra Practice Programs
# 1. Find Largest Number
# a = int(input("First Number: "))
# b = int(input("Second Number: "))

# if a > b:
#     print("Largest:", a)
# else:
#     print("Largest:", b)
# 2. Count Vowels in a String
# text = input("Enter a string: ")
# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print("Vowels:", count)
# 3. Reverse a String
# text = input("Enter a string: ")
# print("Reverse:", text[::-1])
# 4. Find Factorial
# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print("Factorial:", fact)
# 5. Check Prime Number
# num = int(input("Enter a number: "))

# if num < 2:
#     print("Not Prime")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")
# 6. Fibonacci Series
# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# 7. Frequency of Characters
# text = input("Enter a string: ")
# frequency = {}

# for ch in text:
#     frequency[ch] = frequency.get(ch, 0) + 1

# print(frequency)
# Common Errors Beginners Make
# Forgetting indentation.
# Using = instead of == in conditions.
# Trying to modify tuples.
# Accessing a list index that doesn't exist (IndexError).
# Forgetting to convert input() to int or float before arithmetic.
# Confusing is (identity) with == (value equality).
# Exam Tips
# Practice writing code without copying.
# Dry-run programs on paper to understand execution flow.
# Memorize the differences between list, tuple, set, and dictionary.
# Learn common built-in functions: len(), type(), range(), sum(), max(), min(), sorted().
# Focus on loops and conditional statements, as they are frequently tested.
# Frequently Asked Interview/Exam Questions
# What is Python? List its advantages.
# What is the difference between an interpreter and a compiler?
# What is a variable? Explain variable naming rules.
# Differentiate between mutable and immutable data types.
# Compare a list and a tuple.
# What is the difference between a set and a dictionary?
# Explain implicit and explicit type conversion with examples.
# What is the difference between a for loop and a while loop?
# Explain the use of break, continue, and pass.
# Write programs to:
# Find the factorial of a number.
# Check whether a number is prime.
# Print the Fibonacci series.
# Reverse a string.
# Count vowels in a string.
# Find the largest of two or three numbers.
# Quick Revision Summary
# Variables store values in memory and follow naming rules.
# Data Types include int, float, complex, bool, str, list, tuple, set, and dict.
# Lists are ordered and mutable; tuples are ordered and immutable.
# Sets store unique, unordered elements; dictionaries store key-value pairs.
# Use input() to read user input and type() to check a variable's type.
# For loops are best when the number of iterations is known; while loops are useful when repetition depends on a condition.
# Use break to exit a loop, continue to skip an iteration, and pass as a placeholder.