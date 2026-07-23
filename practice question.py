##Student Result Management Program:
# students=[]
# #number of students:
# n=(input("enter the number of students:"))
# for i in range(n):
#     print(f"\nEnter details of student {i+1}")

#     name=input("enter Name: ")
#     roll_no=input("enter roll no:")

#     marks=[]
#     #Taking 5 subject marks
#     for j in range(5):
#         while True:
#             mark=int(input(f"enter marks of Subject {j+1} (0-100):"))
#             if 0<=mark<=100:
#                 marks.append(mark)
#                 break
#             else:
#                 print("invalid marks! please enter marks between 0 and 100.")

#     total=sum(marks)
#     average=total/5

#     #finding Grade
#     if average >=90:
#         grade="A+"
#     elif average >+ 80:
#         grade="A"
#     elif average >=70:
#         grade ="B"
#     elif average >=60:
#         grade = "C"
#     elif average >=40:
#         grade = "D"
#     else:
#         grade = "Fail"

#     #Store data in a list
#     student = [name,roll_no,marks,total,average,grade]
#     students.append(student)

# #Display Result
# print("\n========== STUDENT REPORT ==========")

# for student in students:
#     print("\n---------------------------")
#     print("Name     :", student[0])
#     print("Roll No  :", student[1])
#     print("Marks    :", student[2])
#     print("Total    :", student[3])
#     print("Average  :", round(student[4],2))
#     print("Grade    :", student[5])

# ###PYTHON PROJECT PRACTICE SET:-
# #PROJECT1:STUDENT REPORT CARD SYSTEM
# name=input("enter the name:")
# marks=[]
# for i in range(5):
#     mark=float(input("enter marks of subject {i+1}:"))
#     marks.append(mark)

# total=sum(marks)
# average=total/5
# percentage=average

# if percentage >=90:
#     grade="A+"
# if percentage >=-80:
#     grade="A"
# if percentage >=70:
#     grade="B"
# if percentage >=50:
#     grade="C"    
# else:
#     grade="Fail"

# print("\n---------Report Card----------")
# print("name:",name)        
# print("Marks:",marks)        
# print("Total:",total)        
# print("Average:",average)        
# print("Percentage:",percentage)  
# print("Grade:",grade)        

#PROJECT2:ATM Machine
# balance=5000
# while True:
#     print("\n1.check balance")
#     print("2.Deposit")
#     print("3.Withdraw")
#     print("4.Exit")

#     choice=int(input("enter choice:"))
#     if choice==1:
#         print("current balance:",balance)
#     elif choice==2:
#         amount=float(input("enter amount to deposit:"))
#         balance +=amount
#         print("updated balance:",balance)
#     elif choice==3:
#         amount=float(input("enter amount to withdraw:"))
#         if amount <=balance:
#             balance -=amount
#             print("please collect cash.")
#       

##PROJECT4:LIBRARY MANAGEMENT
library = []

def add_book():
    book = {}

    book["id"] = input("Enter Book ID: ")
    book["name"] = input("Enter Book Name: ")
    book["author"] = input("Enter Author Name: ")
    book["quantity"] = int(input("Enter Quantity: "))

    library.append(book)

    print("Book Added Successfully!")

##project:5:Number guessing game
import random

secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to the Number Guessing Game!")

while True:

    guess = int(input("Enter your guess (1-100): "))

    attempts += 1

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Congratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break

##PROJECT6:CONTACT BOOK
    contacts = []

def add_contact():
    contact = {}

    contact["name"] = input("Enter Name: ")
    contact["phone"] = input("Enter Phone Number: ")
    contact["email"] = input("Enter Email Address: ")

    contacts.append(contact)

    print("Contact Added Successfully!")

##Project7:Shopping Bill
cart = []

def add_item():
    item = {}

    item["name"] = input("Enter Item Name: ")
    item["price"] = float(input("Enter Price: "))
    item["quantity"] = int(input("Enter Quantity: "))

    cart.append(item)

    print("Item Added Successfully!")

##project8:Employee Salary Calculator
employee = {}

def get_employee():

    employee["id"] = input("Enter Employee ID: ")

    employee["name"] = input("Enter Employee Name: ")

    employee["basic"] = float(input("Enter Basic Salary: "))

##project9:word counter
def get_text():

    text = input("Enter a paragraph: ")

    return text

##project10:bank account
account = {}

def create_account():
    account["number"] = input("Enter Account Number: ")
    account["name"] = input("Enter Account Holder Name: ")
    account["balance"] = float(input("Enter Initial Balance: "))

    print("Account Created Successfully!")
