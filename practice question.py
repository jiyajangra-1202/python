##Student Result Management Program:
students=[]
#number of students:
n=(input("enter the number of students:"))
for i in range(n):
    print(f"\nEnter details of student {i+1}")

    name=input("enter Name: ")
    roll_no=input("enter roll no:")

    marks=[]
    #Taking 5 subject marks
    for j in range(5):
        while True:
            mark=int(input(f"enter marks of Subject {j+1} (0-100):"))
            if 0<=mark<=100:
                marks.append(mark)
                break
            else:
                print("invalid marks! please enter marks between 0 and 100.")

    total=sum(marks)
    average=total/5

    #finding Grade
    if average >=90:
        grade="A+"
    elif average >+ 80:
        grade="A"
    elif average >=70:
        grade ="B"
    elif average >=60:
        grade = "C"
    elif average >=40:
        grade = "D"
    else:
        grade = "Fail"

    #Store data in a list
    student = [name,roll_no,marks,total,average,grade]
    students.append(student)

#Display Result
print("\n========== STUDENT REPORT ==========")

for student in students:
    print("\n---------------------------")
    print("Name     :", student[0])
    print("Roll No  :", student[1])
    print("Marks    :", student[2])
    print("Total    :", student[3])
    print("Average  :", round(student[4],2))
    print("Grade    :", student[5])

###PYTHON PROJECT PRACTICE SET:-
#PROJECT1:STUDENT REPORT CARD SYSTEM
name=input("enter the name:")
marks=[]
for i in range(5):
    mark=float(input("enter marks of subject {i+1}:"))
    marks.append(mark)

total=sum(marks)
average=total/5
percentage=average

if percentage >=90:
    grade="A+"
if percentage >=-80:
    grade="A"
if percentage >=70:
    grade="B"
if percentage >=50:
    grade="C"    
else:
    grade="Fail"

print("\n---------Report Card----------")
print("name:",name)        
print("Marks:",marks)        
print("Total:",total)        
print("Average:",average)        
print("Percentage:",percentage)  
print("Grade:",grade)        

#PROJECT2:ATM Machine
balance=5000
while True:
    print("\n1.check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=int(input("enter choice:"))
    if choice==1:
        print("current balance:",balance)
    elif choice==2:
        amount=float(input("enter amount to deposit:"))
        balance +=amount
        print("updated balance:",balance)
    elif choice==3:
        amount=float(input("enter amount to withdraw:"))
        if amount <=balance:
            balance -=amount
            print("please collect cash.")
        else:
            print("insufficient balance")
    elif choice==4:
        print("Thank you!")
        break
    else:
        print("invalid choice")

#PROJECT3:PASSWORD STRENGTH CHECKER:-
password=input("enter password:")
upper=False
lower=False
digit=False
special=False

for ch in password:
    if ch.isupper():
        upper=True
    elif ch.islower():
        lower=True
    elif ch.isdigit():
        digit=True
    else:
        special=True

if len(password) >=8 and upper and lower and digit and special:
    print("Strong password")
else:
    print("weak password")    
