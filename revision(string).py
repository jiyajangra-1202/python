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
        count==1
print("Vowels=",count)           


