#operators(symbol or keyword that performs an operation on one or more values)
#LOGICAL OPERATORS:-
age=25
has_ticket=True
if age>=18 and has_ticket:
 print("entry allowed")
else:
 print("entry denied.")#and operator

 day="saturday"
 if day=="saturday"  or day=="sunday":
  print("it the weekend!")
 else:
  print("it  is a weekday")#or operator

  is_raining=False
  if not is_raining:
   print("lets go outside.")
   
# age=15
# has_license=True
# has_car=False
# if age>=18 or (has_license or has_car):
#  print("you can drive")
# else:
#  print("you need a license or a car firstly")#mixed of many operator

 username="admin"
 password="1234"
 entered_username=input("username:")
 entered_password=input("password:")
 if entered_password==username and entered_password==password:
   print("login successful")
 else:
  print("incorrect username or password")

  score=int(input("Enter your score:"))
  attended_class=True
  if score>=60:
   if attended_class:
    print("you passed with attendance credit.")
   else:
    print("you passed,but attended is missing.")
  else:
     print("you did not pass.") 