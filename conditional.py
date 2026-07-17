#Conditional Satatements in python(allow a program to make decision.)
#TYPES OF CONDITIONAL STATEMENTS:-
#if statement,if..else statement,nested if statement
#Syntax of if statement:-
age=19
if age>=18:
 print("you are eligible to vote.")#if statement(only when the condition is true)
 print(input("ENTER YOUR AGE:"))
 if age>=18:
  print("you are eligible to vote")#if statement for giving user input
  #Syntax of if..else statement:-
  age=16
  if age>=18:
   print("you arre eligible for voting.")
  else:
   print("you are not eligible for voting.")#if..else statement(when one condition is true,one block executes.)
   #Syntax of if..elif..else(used when there are multiple condition)
   marks=85
   if marks>=90:
    print("grade A+")
   elif marks>=80:
    print("grade B+")
   elif marks>=70:
    print("Grade B")
   elif marks>=60:
    print("Grade C=")
   elif marks>=50:
    print("Grade C")
   else:
    print("failed")
    #Syntax of Nested if(An if statement inside another if.)
    age=22
    citizen=True
    if age>=18:
     if citizen:
      print("Eligible to vote")
     else:
      print("Not a Citizen")
else:
 print("Too Young")
#Syntax of short-hand if(used for a single statement)
age=20
if age>=18: print("Adult")
#Short-hand if..else(Ternary Operator)
# age=17
# print("Adult") if age >= 18 else 
# print("Minor")
#Using Logical operators
#AND Operator
age=20
marks=80
if age>=18 and marks>=75:
 print("Eligible")#Both conditions must be True.
 #OR Operator
 age=16
 special=True
 if age>=18 or special:
  print("Allowed")#At least one condition must be True
  #NOT Operator
  is_raining=False
  if not is_raining:
   print("Go outside") #Reverses the condition.


Java