#loop is used to execute a block of code repeatedly
#Using a loop
for i in range(5):
    print("Hello World")
#TYPES OF LOOPS IN PYTHON
#Syntax of for loop(used to iterate over a sequences)
# it used in string,list,tuple,set,dictionary or range
for i in range(1,6):
    print(i)    #print numbers
    for i in range(5):
        print("Jiya")#print a name 5 times
        #loop through a string
name="python"   
for letter in name:
    print(letter)
    #loop through a list
    fruits=["apple","banana","orange"]
    for fruit in fruits:
        print(fruit)

#range
for x in range(2,16):
    print(x)

    for x in range(0,20,3):
        print(x)#even number
  #while loop(executes as long as condition is True)

# count=0
# while count<5:
#     print(count)
#     count +=1
# password="1234"
# while password.strip() !="secrect":
#     password=input("enter your password:")
#     print("access granted")    

# total=0
# number=int(input("enter a number:"))

# while number !=0:
#     total += number
#     number=int(input("enter another number:"))

# print("Total:",total)  

# secret_number=7
# guess=0
# while guess !=secret_number:
#     guess=int(input("guess the number:"))

# print("Correct!")    


#LOOP CONTROL STATEMENTS:-
# IT CONTROL THE FLOW OF LOOPS.
##1.break:stops the loop immediately.
# for i in range(1,6):
#     if i==4:
#         break
#     print(i)    
# words="Artifical"
# for x in words:
#     print(x)
# ##2.continue:-skips the current iteration and moves to the next one.
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)
#Sum of 1 to 20 using for loop
# sum=0
# for i in range(1,21):
#  sum=sum+i
# print("sum=",sum)
numbers=[1,2,3,4,5]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)