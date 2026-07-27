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