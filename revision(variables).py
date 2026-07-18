#Variables in python:-used to store data in the computer memory.
#Variables as a container that holds information.
# Ques1.
# name="Jiya Kumari"
# age=19
# height=5.1
# student=True
# print(name)
# print(age)
# print(height)
# print(student)#different data types
# # Ques2.
# a=10
# b=20
# print(a)
# print(b)
# # Ques3.
# a=10
# a=50
# print(a)
# # Ques4.
# x=5
# y=10
# z=15
# print(x,y,z)
# # Ques5.
# a=100
# a=b
# b=a
# c=a
# print(a,b,c)
# #Ques6.
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(student))
# #Ques7.
# a=100
# b=67
# c=98
# del a
# print(b,c)
#LEVEL2:EASY PROGRAMS
#ques8.
# name=input("enter your name:")
# age=input("enter  your age:")
# print(name)
# print(age)
# #Ques9.
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# c=int(input("enter the value of c:"))
# sum=a+b+c
# mul=a*b*c
# average=(a+b+c)/3
# print(a)
# print(b)
# print("sum=",sum)
# print("mul:",mul)
# print("average:",average)
# #ques10.
# a=int(input("enter the value of a:"))
# square=a*a
# print("a=",a)
# print("square=",square)
#ques11.
a=10
b=20
a,b=b,a
#after swapping
print(a)
print(b)
#ques12.covert celsius to fahrenheit
# celsius=float(input("enter temp in celsius:"))
# fahrenheit=(celsius*9/5)+32
# print("temp in  fahrenheit=",fahrenheit)
#Intermediate Level:-
#ques13.store your first name and second name separately and print the full name
# first_name="Jiya"
# last_name="kumari"
# full_name=first_name+last_name
# print(full_name)
#ques14.create five variables and print them in one print() statement
# a=12
# b=13
# c=14
# d=15
# e=16
# print(a,b,c,d,e)
#ques15.take marks of five subject and calculate the total
# maths=int(input("marks of maths:"))
# phy=int(input("marks of phy:"))
# chem=int(input("marks of chem:"))
# bio=int(input("marks of bio:"))
# eng=int(input("marks of eng:"))
# percentage=(maths+phy+chem+bio+eng)/5
# print("percentage:",percentage)
#ques16.store two string and join them
# first_name="jiya"
# second_name="jangra"
# join=first_name+second_name
# print(join)
# #ques17.exchange the three variables
# a=12
# b=98
# c=67
# print("before exchanging:")
# print("a:",a)
# print("b:",b)
# print("c:",c)
# a,b,c=b,c,a
# print("after exchanging:")
# print("a:",a)
# print("b:",b)
# print("c:",c)
# #ques18.use multiple assignment to assign five values
# a,b,c,d,e=10,20,30,40,50
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# #ques19.find the largest of two numbers using variables.
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# if num1>num2:
#     print("largest number:",num1)
# else:
#     print("largest number:",num2)
# #ques20.take the length and breadth of a rectangle and calculate both the area and perimeter
# length=int(input("enter the length:"))
# breadth=int(input("enter the breadth:"))
# area=length*breadth
# perimeter=2*(length+breadth)
# print("area:",area)
# print("perimeter:",perimeter)
# #ques21.predict the output 
# a=10
# b=a
# a=20
# print(a)
# print(b)#output:-20 10
# #ques22.predict the output
# x=y=z=5
# x=10
# print(x,y,z)#output:-10 5 5
# #ques23.predict the output:-
# a,b=5,10
# a,b=b,a
# print(a,b)#output:-10 5
# #ques24.predict the output:-
# x=5
# x=x+10
# print(x)#output:-15
# #ques25.predict the output:-
# a=5
# b=2
# c=a**b
# print(c)
# #ques26.predict the output:-
# a="10"
# b=20
# print(a,b)#output:-10 20
# ##W.A.P that takes a students name,roll number,age,and marks as input and print all the information neatly.
student_name=(input("enter student's name:"))
roll_number=(input("enter your roll number:"))
age=int(input("enter your age:"))
marks=(input("enter your marks"))
print("student_name:",student_name)
print("roll_number:",roll_number)
print("age:",age)
print("marks:",marks)