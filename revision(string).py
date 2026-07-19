Name="jiya"
print(Name)
Language="Python"
Text="Programming"
Subject="Computer Science"
message="Hello World"
practical="python programming"
print(Language[0])#first character
print(Text[10])#last character
print(len(Subject))#length
print(message.upper())#uppercase
print(Language.lower())#lowercase
print(practical.capitalize())#capitalize
print(practical.count("p"))#count
print(practical.startswith("py"))#startwith
print(message.endswith("ld"))#endwith
print(Name[::-1])#reverse slicing
print(Text[::2])#print every second character
a="Hello"
b="python"
print(a+b)
concatenate=a+b
print(concatenate)#Concatenate
print(Text*6)#repeat many times
Text="12345"
print(Text.isdigit())
Name=input("enter your  name:")
print(len(Name),Name)#take a string as input and print its length
for ch in Name:
    print(ch)#print each character using for loop
Text="I AM a python learner"
count=0
for ch in Text.lower():
    if ch in "aeiou":
        count+=1
print("Vowels=",count)#count vowels
text="Iam a programmer that can work on python language"
count=0
for ch in Text.lower():
    if ch.isalpha() and ch not  in "aeiou":
        count+=1
print("number of consonants=",count)#count consonant
text=input("enter a string:")   
count=text.count(" ")
print("Number of spaces=",count)#number of  space
message=input("enter your string:")
upper=0
lower=0
for ch in message:
    if ch.isupper():
        upper +=1
    elif ch.islower()  :
        lower +=1
print("Uppercase letters=",upper)
print("Lowercase letters=",lower)    #count the number of uppercase and lowercase letters
text=input("enter a string:")
print(text.replace(" ","-"))#replace every space with "-"
text=input("enter a sting:")
print(text.strip())#remove leading aand trailing spacces
word=input("enter a word:")
if word==word[::-1]:
    print("palindrome")
else:
    print("not palindrome")#palindrome
        








