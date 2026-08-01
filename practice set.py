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

# Python is a high-level, interpreted, object-oriented, and general-purpose programming language. It is one of the easiest programming languages because its syntax is simple and similar to English.

# Python is widely used in:

# Artificial Intelligence
# Machine Learning
# Data Science
# Automation
# Web Development
# Cyber Security
# Game Development
# 2. Conditional Statements
# What is a Conditional Statement?

# A conditional statement is used to make decisions in a program.

# It executes a block of code based on whether a condition is True or False.

# Real-Life Example

# Suppose you go to an ATM.

# If your PIN is correct:

# Money is withdrawn.

# Otherwise:

# Transaction is cancelled.

# Similarly, Python checks conditions.

# Types of Conditional Statements
# if
# if-else
# if-elif-else
# Nested if
# 2.1 if Statement
# Syntax
# if condition:
#     statement
# Example
# age = 20

# if age >= 18:
#     print("Eligible for Voting")

# Output

# Eligible for Voting
# Flow

# Condition → True → Execute

# Condition → False → Skip

# Example 2
# marks = 85

# if marks >= 40:
#     print("Pass")

# Output

# Pass
# 2.2 if-else Statement
# Syntax
# if condition:
#     statements
# else:
#     statements
# Example
# age = 15

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# Output

# Not Eligible
# Example 2

# Check Even or Odd

# num = int(input("Enter Number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")
# 2.3 if-elif-else

# Used when there are multiple conditions.

# Syntax
# if condition:
#     statement

# elif condition:
#     statement

# else:
#     statement

# Example

# marks = int(input("Enter Marks: "))

# if marks >= 90:
#     print("Grade A")

# elif marks >= 75:
#     print("Grade B")

# elif marks >= 60:
#     print("Grade C")

# elif marks >= 40:
#     print("Grade D")

# else:
#     print("Fail")
# 2.4 Nested if

# One if statement inside another.

# Example

# age = 25
# salary = 50000

# if age >= 18:

#     if salary >= 30000:
#         print("Loan Approved")

#     else:
#         print("Low Salary")

# else:
#     print("Minor")
# Logical Operators in Conditions
# Operator	Meaning
# and	Both conditions True
# or	Any one condition True
# not	Reverse condition

# Example

# age = 20
# citizen = True

# if age >= 18 and citizen:
#     print("Eligible")
# Important Points
# Indentation is compulsory.
# Conditions always return True or False.
# Use == for comparison.
# Never confuse = with ==.
# Practice Programs
# Largest among Three Numbers
# a = int(input("First: "))
# b = int(input("Second: "))
# c = int(input("Third: "))

# if a > b and a > c:
#     print(a)

# elif b > c:
#     print(b)

# else:
#     print(c)
# Leap Year
# year = int(input("Enter Year: "))

# if year % 400 == 0:
#     print("Leap Year")

# elif year % 100 == 0:
#     print("Not Leap Year")

# elif year % 4 == 0:
#     print("Leap Year")

# else:
#     print("Not Leap Year")
# 3. String
# Definition

# A string is a collection (sequence) of characters enclosed in:

# Single quotes ' '
# Double quotes " "
# Triple quotes ''' ''' or """ """

# Example

# name = "Python"

# city = 'Delhi'

# paragraph = """Python is easy."""
# String Characteristics
# Ordered
# Immutable
# Allows duplicate characters
# Supports indexing
# Supports slicing
# Indexing
# P  y  t  h  o  n

# 0  1  2  3  4  5

# Negative Index

# -6 -5 -4 -3 -2 -1

# Example

# text = "Python"

# print(text[0])
# print(text[-1])

# Output

# P
# n
# Slicing

# Syntax

# string[start:end:step]

# Example

# text = "Programming"

# print(text[0:7])
# print(text[3:])
# print(text[:5])
# print(text[::2])

# Output

# Program
# gramming
# Progr
# Pormig
# Common String Methods
# text = "python programming"

# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.replace("python","Java"))
# print(text.find("program"))
# print(text.count("m"))
# print(len(text))
# print(text.split())
# String Operators

# Concatenation

# a = "Hello"

# b = "World"

# print(a + " " + b)

# Repetition

# print("Hi " * 3)
# Looping Through a String
# word = "Python"

# for ch in word:
#     print(ch)
# String Programs
# Reverse String
# text = input("Enter String: ")

# print(text[::-1])
# Palindrome
# text = input("Enter String: ")

# if text == text[::-1]:
#     print("Palindrome")

# else:
#     print("Not Palindrome")
# Count Vowels
# text = input("Enter String: ")

# count = 0

# for ch in text.lower():

#     if ch in "aeiou":
#         count += 1

# print(count)
# 4. List
# Definition

# A list is an ordered, mutable collection that can store multiple values of different data types.

# Example

# numbers = [10,20,30,40]
# Features
# Ordered
# Mutable
# Duplicate values allowed
# Dynamic size
# Supports indexing and slicing
# Accessing Elements
# fruits = ["Apple","Banana","Mango"]

# print(fruits[0])
# print(fruits[-1])
# Updating List
# fruits[1] = "Orange"

# print(fruits)
# Important Methods

# Append

# fruits.append("Kiwi")

# Insert

# fruits.insert(1,"Pineapple")

# Remove

# fruits.remove("Apple")

# Pop

# fruits.pop()

# Sort

# numbers.sort()

# Reverse

# numbers.reverse()

# Length

# len(numbers)
# List Traversal
# numbers = [10,20,30]

# for i in numbers:
#     print(i)
# Nested List
# matrix = [

# [1,2],

# [3,4]

# ]

# print(matrix[1][0])

# Output

# 3
# List Programs
# Sum of List
# numbers = [10,20,30,40]

# print(sum(numbers))
# Largest Number
# numbers = [5,9,12,7]

# print(max(numbers))
# Remove Duplicates
# numbers = [1,2,2,3,4,4]

# unique = list(set(numbers))

# print(unique)

# Note: Converting to a set removes duplicates but may change the order of elements.

# Find Second Largest
# numbers = [15,60,25,70,45]

# numbers.sort()

# print(numbers[-2])
# List Comprehension
# square = [x*x for x in range(1,6)]

# print(square)

# Output

# [1,4,9,16,25]
# 5. Tuple
# Definition

# A tuple is an ordered, immutable collection of elements.

# Example

# numbers = (10,20,30)
# Features
# Ordered
# Immutable
# Duplicate values allowed
# Faster than list
# Supports indexing
# Access Elements
# numbers = (5,10,15)

# print(numbers[0])
# Tuple Packing
# student = ("Aman",20,"Delhi")
# Tuple Unpacking
# name, age, city = student

# print(name)
# print(age)
# Tuple Methods

# Count

# numbers = (10,20,10,40)

# print(numbers.count(10))

# Index

# print(numbers.index(20))
# Tuple Programs
# Sum
# numbers = (10,20,30)

# print(sum(numbers))
# Maximum
# numbers = (15,22,50)

# print(max(numbers))
# Minimum
# numbers = (15,22,50)

# print(min(numbers))
# Tuple Traversal
# numbers = (10,20,30)

# for i in numbers:
#     print(i)
# 6. Difference Between List and Tuple
# Feature	List	Tuple
# Syntax	[]	()
# Mutable	Yes	No
# Ordered	Yes	Yes
# Duplicate Elements	Yes	Yes
# Indexing	Yes	Yes
# Slicing	Yes	Yes
# Performance	Slightly slower	Faster
# Memory Usage	Higher	Lower
# 7. Comprehensive Practice Programs
# Program 1: Student Result
# marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Very Good")

elif marks >= 50:
    print("Good")

elif marks >= 35:
    print("Pass")

else:
    print("Fail")
# Program 2: Count Digits, Letters, and Special Characters
# text = input("Enter Text: ")

# letters = digits = special = 0

# for ch in text:

#     if ch.isalpha():
#         letters += 1

#     elif ch.isdigit():
#         digits += 1

#     else:
#         special += 1

# print("Letters =", letters)
# print("Digits =", digits)
# print("Special =", special)
# Program 3: Merge Two Lists
# list1 = [1,2,3]
# list2 = [4,5,6]

# merged = list1 + list2

# print(merged)
# Program 4: Frequency of Each Character
# text = input("Enter String: ")

# frequency = {}

# for ch in text:
#     frequency[ch] = frequency.get(ch, 0) + 1

# print(frequency)
# Program 5: Search an Element in a Tuple
# numbers = (10,20,30,40)

# item = int(input("Enter Number: "))

# if item in numbers:
#     print("Found")

# else:
#     print("Not Found")
# 8. Frequently Asked Questions
# What is a conditional statement?
# Explain the difference between if, if-else, and if-elif-else.
# What is a nested if statement?
# What is a string? Explain indexing and slicing.
# What are common string methods?
# What is a list? Why is it mutable?
# Explain list comprehension with an example.
# What is a tuple? Why is it immutable?
# Compare lists and tuples.
# When should you use a tuple instead of a list?
# 9. Important Examination Points
# Remember the syntax of all conditional statements.
# Practice string indexing and slicing thoroughly.
# Learn common string methods (upper(), lower(), split(), replace(), find(), count()).
# Be comfortable using list methods (append(), insert(), remove(), pop(), sort(), reverse()).
# Understand that tuples cannot be modified after creation.
# Know the difference between mutable (list) and immutable (tuple) objects.
# Practice writing programs using loops with strings, lists, and tuples.
# 10. Quick Revision Notes
# Conditional Statements
# Used for decision-making.
# Types: if, if-else, if-elif-else, nested if.
# Logical operators: and, or, not.
# Strings
# Ordered and immutable sequence of characters.
# Support indexing, slicing, concatenation, and iteration.
# Frequently used methods include upper(), lower(), replace(), find(), count(), split(), and join().
# Lists
# Ordered, mutable collections.
# Can contain mixed data types and duplicate values.
# Common methods: append(), extend(), insert(), remove(), pop(), sort(), reverse(), clear(), and copy().
# Tuples
# Ordered, immutable collections.
# Suitable for fixed data that should not change.
# Support indexing, slicing, count(), and index().
# Recommended Practice

# To master these topics, write and test programs for:

# Even/odd number checker
# Largest of three numbers
# Grade calculator
# Palindrome checker
# Vowel and consonant counter
# Word frequency counter
# List sorting (ascending and descending)
# Removing duplicates while preserving order
# Matrix (nested list) operations
# Tuple packing and unpacking
# Searching and counting elements in tuples


# python is a high-level, interpreted, object-oriented, and general-purpose programming language developed by Guido van Rossum in 1991. It is widely used because of its simple syntax and readability.

# Applications of Python
# Artificial Intelligence (AI)
# Machine Learning (ML)
# Data Science
# Web Development
# Automation
# Cyber Security
# Software Development
# Game Development
# Cloud Computing
# Features of Python
# Easy to Learn
# Open Source
# Platform Independent
# Large Community Support
# Extensive Libraries
# Interpreted Language
# Object-Oriented
# 1. Python Loops
# Definition

# A loop is used to execute a block of code repeatedly until a specified condition becomes false.

# Loops reduce code repetition and make programs efficient.

# Types of Loops

# There are two types of loops in Python:

# for loop
# while loop
# A. for Loop
# Syntax
# for variable in sequence:
#     statement
# Example 1: Print Numbers
# for i in range(1, 6):
#     print(i)
# Output
# 1
# 2
# 3
# 4
# 5
# Example 2: Print Student Names
# students = ["Ram", "Shyam", "Mohan"]

# for name in students:
#     print(name)
# Output
# Ram
# Shyam
# Mohan
# Example 3: Sum of Numbers
# total = 0

# for i in range(1, 11):
#     total += i

# print("Sum =", total)
# Output
# Sum = 55
# B. while Loop
# Syntax
# while condition:
#     statement
# Example
# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# Output

# 1
# 2
# 3
# 4
# 5
# Loop Control Statements
# 1. break

# Stops the loop immediately.

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# Output

# 0
# 1
# 2
# 3
# 4
# 2. continue

# Skips the current iteration.

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

# Output

# 0
# 1
# 2
# 4
# 5
# 3. pass

# Acts as a placeholder.

# for i in range(5):
#     pass
# Nested Loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i, j)

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
# Real-Life Example

# Printing attendance of students.

# students = ["Aman", "Riya", "Karan"]

# for student in students:
#     print(student, "Present")
# Advantages of Loops
# Reduce repetitive code
# Save time
# Easy to maintain
# Improve readability
# Suitable for automation
# Important Interview Questions
# Difference between for and while loop?
# What is nested loop?
# Difference between break and continue?
# Can loops be infinite?
# Practice Programs
# Print Even Numbers
# for i in range(2,21,2):
#     print(i)
# Multiplication Table
# num = 7

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
# Factorial using Loop
# n = 5
# fact = 1

# for i in range(1,n+1):
#     fact *= i

# print(fact)
# 2. Python Sets
# Definition

# A Set is an unordered, mutable collection of unique elements.

# Duplicate values are automatically removed.
# Sets do not support indexing.
# Creating Sets
# fruits = {"Apple", "Banana", "Orange"}
# print(fruits)
# Empty Set
# s = set()

# print(type(s))
# Duplicate Removal
# numbers = {10,20,30,20,10}

# print(numbers)

# Output

# {10,20,30}
# Set Operations
# Add Element
# students = {"Ram","Shyam"}

# students.add("Mohan")

# print(students)
# Remove Element
# students.remove("Ram")
# Discard
# students.discard("Rahul")

# (No error if element doesn't exist.)

# Union
# A = {1,2,3}
# B = {3,4,5}

# print(A | B)

# Output

# {1,2,3,4,5}
# Intersection
# print(A & B)

# Output

# {3}
# Difference
# print(A - B)

# Output

# {1,2}
# Symmetric Difference
# print(A ^ B)

# Output

# {1,2,4,5}
# Membership Testing
# colors = {"Red","Blue","Green"}

# print("Red" in colors)

# Output

# True
# Applications of Sets
# Remove duplicates
# Database operations
# Mathematical computations
# Search optimization
# Data analysis
# Advantages
# Fast searching
# Unique elements
# Mathematical operations
# Memory efficient
# Practice Program

# Find common subjects.

# student1 = {"Python","Java","C"}

# student2 = {"Python","C++","Java"}

# print(student1 & student2)
# 3. Python Dictionary
# Definition

# A Dictionary stores data as key-value pairs.

# Keys are unique.

# Creating Dictionary
# student = {
#     "Name":"Amit",
#     "Age":20,
#     "Course":"BCA"
# }

# print(student)
# Access Values
# print(student["Name"])
# Using get()
# print(student.get("Age"))
# Add New Item
# student["City"] = "Delhi"

# print(student)
# Update Value
# student["Age"] = 21
# Delete Item
# del student["Course"]
# Loop Through Dictionary
# for key,value in student.items():
#     print(key,"=",value)
# Dictionary Methods
# Method	Purpose
# keys()	Returns all keys
# values()	Returns all values
# items()	Returns key-value pairs
# update()	Updates dictionary
# pop()	Removes item
# clear()	Removes all items
# Nested Dictionary
# students = {
#     101:{
#         "Name":"Rahul",
#         "Marks":85
#     },
#     102:{
#         "Name":"Priya",
#         "Marks":91
#     }
# }

# print(students[102]["Marks"])
# Advantages
# Fast lookup
# Organized data
# Flexible
# Dynamic
# Real-Life Example
# employee = {
#     "ID":101,
#     "Name":"Raj",
#     "Salary":45000,
#     "Department":"HR"
# }

# for key,value in employee.items():
#     print(key,":",value)
# Practice Program

# Count frequency of characters.

# text = "python"

# freq = {}

# for ch in text:
#     freq[ch] = freq.get(ch,0)+1

# print(freq)

# Output

# {'p':1,'y':1,'t':1,'h':1,'o':1,'n':1}
# 4. Recursion
# Definition

# Recursion is a programming technique in which a function calls itself to solve a problem.

# Every recursive function must have:

# Base Case: Stops the recursion.
# Recursive Case: Calls itself with a smaller or simpler problem.

# Without a base case, recursion will continue indefinitely until Python raises a RecursionError.

# Syntax
# def function_name(parameters):
#     if base_condition:
#         return value
#     return function_name(modified_parameters)
# Example 1: Print Numbers Using Recursion
# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n - 1)
#     print(n)

# print_numbers(5)
# Output
# 1
# 2
# 3
# 4
# 5
# Example 2: Factorial Using Recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))
# Output
# 120
# Example 3: Fibonacci Series
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(8):
#     print(fibonacci(i), end=" ")
# Output
# 0 1 1 2 3 5 8 13
# Example 4: Sum of Digits
# def sum_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_digits(n // 10)

# print(sum_digits(12345))
# Output
# 15
# Example 5: Reverse a String
# def reverse_string(text):
#     if len(text) == 0:
#         return ""
#     return reverse_string(text[1:]) + text[0]

# print(reverse_string("Python"))
# Output
# nohtyP
# Advantages of Recursion
# Simplifies complex problems.
# Useful for tree and graph traversal.
# Makes divide-and-conquer algorithms easier (e.g., Merge Sort, Quick Sort).
# Produces elegant code for naturally recursive problems.
# Limitations of Recursion
# Higher memory usage due to the call stack.
# Can be slower than iteration for simple tasks.
# Deep recursion may cause a RecursionError.
# Requires a correct base case to avoid infinite recursion.
# Comparison Table
# Feature	Loop	Recursion
# Repeats code	Yes	Yes
# Uses function calls	No	Yes
# Memory usage	Low	Higher
# Speed	Usually faster	Often slower
# Best for	Simple repetition	Problems that naturally divide into smaller subproblems
# Comprehensive Practice Programs
# Program 1: Count Word Frequency Using a Dictionary
# sentence = "python is easy and python is powerful"

# words = sentence.split()
# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print(frequency)
# Program 2: Remove Duplicate Elements Using a Set
# numbers = [10, 20, 30, 20, 40, 10, 50]

# unique_numbers = list(set(numbers))

# print("Original List :", numbers)
# print("Unique List   :", unique_numbers)
# Program 3: Student Marks Management
# students = {
#     "Aman": 85,
#     "Riya": 91,
#     "Karan": 78,
#     "Neha": 95
# }

# highest = max(students, key=students.get)

# print("Top Student:", highest)
# print("Marks:", students[highest])
# Program 4: Prime Numbers Using Loops
# for num in range(2, 21):
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)
# Program 5: Recursive Binary Search
# def binary_search(arr, target, low, high):
#     if low > high:
#         return -1

#     mid = (low + high) // 2

#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, target, low, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, high)

# numbers = [2, 5, 8, 12, 16, 23, 38]
# target = 16

# index = binary_search(numbers, target, 0, len(numbers) - 1)

# print("Element found at index:", index)
# Key Points to Remember
# Loops (for, while) automate repetitive tasks.
# Sets store only unique elements and support efficient mathematical set operations.
# Dictionaries organize data as key-value pairs with fast lookup by key.
# Recursion solves problems by breaking them into smaller instances of the same problem and always requires a base case.
# Choose loops for straightforward repetition and recursion for problems with recursive structures (such as trees, divide-and-conquer algorithms, and recursive mathematical definitions).

# 1. Problem Statement

# Write a Python program to print "Hello World" exactly 10 times using a loop.

# 2. Objective
# Learn the for loop.
# Understand the use of range().
# Practice repetitive execution.
# 3. Theory

# A loop allows a block of code to execute repeatedly.

# Python provides:

# for loop
# while loop

# Since we know the number of repetitions (10), a for loop is the best choice.

# 4. Syntax
# for variable in range(start, stop, step):
#     statements

# Example

# for i in range(5):
#     print(i)

# Output

# 0
# 1
# 2
# 3
# 4
# 5. Algorithm
# Start.
# Run a loop 10 times.
# Print "Hello World" in each iteration.
# Stop.
# 6. Flow of Execution
# Start
#    │
#    ▼
# Loop starts
#    │
# Print Hello World
#    │
# Decrease remaining iterations
#    │
# Loop completed?
#    │
# Yes
#    ▼
# Stop
# 7. Python Code
# for i in range(10):
#     print("Hello World")
# 8. Line-by-Line Explanation
# for i in range(10):
# Creates a loop.
# range(10) generates numbers from 0 to 9.
# Total iterations = 10.
# print("Hello World")

# Prints the text in every iteration.

# 9. Sample Output
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World
# 10. Dry Run
# Iteration	Value of i	Output
# 1	0	Hello World
# 2	1	Hello World
# 3	2	Hello World
# 4	3	Hello World
# 5	4	Hello World
# 6	5	Hello World
# 7	6	Hello World
# 8	7	Hello World
# 9	8	Hello World
# 10	9	Hello World
# 11. Time Complexity
# O(n)

# where n = 10

# 12. Space Complexity
# O(1)
# 13. Alternative Method
# count = 1

# while count <= 10:
#     print("Hello World")
#     count += 1
# 14. Real-world Application
# Sending reminders
# Displaying repeated messages
# Running a task multiple times
# Generating repeated reports
# 15. Common Mistakes

# ❌ Forgetting indentation

# for i in range(10):
# print("Hello")

# Correct

# for i in range(10):
#     print("Hello")
# 16. Interview Questions

# Q1. Why is a for loop better than a while loop here?

# Answer: Because the number of iterations is known.

# 17. Viva Questions

# Q. What does range(10) return?

# Answer: Numbers from 0 to 9.

# 18. Practice Questions
# Print your name 20 times.
# Print "Python" 15 times.
# Print "Welcome" 100 times.
# Program 2: Print Numbers from 1 to 100
# 1. Problem Statement

# Write a Python program to print all numbers from 1 to 100 using a loop.

# 2. Objective
# Learn how to use range(start, stop).
# Understand sequential iteration.
# 3. Algorithm
# Start.
# Use a for loop with range(1, 101).
# Print each number.
# Stop.
# 4. Python Code
# for i in range(1, 101):
#     print(i)
# 5. Line-by-Line Explanation
# for i in range(1, 101):
# Starts from 1.
# Stops before 101, so the last value is 100.
# print(i)

# Prints the current number.

# 6. Sample Output (First 10 Numbers)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ...
# 100
# 7. Dry Run
# Iteration	i	Output
# 1	1	1
# 2	2	2
# 3	3	3
# 4	4	4
# 5	5	5
# ...	...	...
# 100	100	100
# 8. Time Complexity
# O(n)

# where n = 100

# 9. Space Complexity
# O(1)
# 10. Alternative Method
# i = 1

# while i <= 100:
#     print(i)
#     i += 1
# 11. Real-world Application
# Generating serial numbers
# Printing roll numbers
# Creating numbered reports
# Displaying ranking lists
# 12. Common Mistakes

# ❌ Using:

# range(1,100)

# This prints only 1–99.

# Correct:

# range(1,101)
# 13. Interview Questions

# Q. Why does range(1, 101) print up to 100?

# Answer: The stop value in range() is exclusive, so 101 is not included.

# 14. Viva Questions

# Q. What are the parameters of range()?

# Answer: range(start, stop, step).

# 15. Practice Questions
# Print numbers from 50 to 100.
# Print numbers from 100 down to 1.
# Print every fifth number from 1 to 100.

# This is the level of detail I will use for all remaining 55 programs, including:

# Print even numbers
# Print odd numbers
# Sum of first N numbers
# Multiplication table
# Factorial using loop
# Fibonacci series
# Reverse a number
# Palindrome number
# Prime number
# Armstrong number
# Star and pyramid patterns
# Menu-driven calculator
# and then all Sets, Dictionary, and Recursion programs in the same structured format.


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
# numbers = [10, 45, 32, 78, 56]

# numbers = sorted(set(numbers))

# print("Second Largest =", numbers[-2])
# Output
# Second Largest = 56
# Program 16 – Count Frequency of an Element
# numbers = [10, 20, 20, 30, 20, 40]

# count = numbers.count(20)

# print("Frequency =", count)
# Output
# Frequency = 3
# Program 17 – Rotate a List (Left Rotation by One Position)
numbers = [10, 20, 30, 40, 50]

rotated = numbers[1:] + numbers[:1]

print(rotated)
Output
[20, 30, 40, 50, 10]
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