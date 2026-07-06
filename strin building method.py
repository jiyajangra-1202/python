#Types of string
Message='I am a python learner and python is a awesome proramming language'#single quoted string
print(Message)
Name="Jiya Jangra"
print(Name)#double-quoted string
Text="""Python is a essay language just like a english language"""
print(Text)#triple-quoted string
#Building-Methods of string
First="Hello"
Second="World"
result=First+" "+Second
print(result)#string concatenation
text="Hiiii everyone" 
print(text*12)#repeitition
words=["Python","is","essay"]
result=" ".join(words)
print(result)#join string
name="Mahii"
Age=12
print(f"My name is {name} and I am {Age} years old.")#Using f-String
print("My name is {} and I am {} years old" .format(name,Age))#using format string
Name="Mahak"
Marks=98
print("Name: %s,Marks:%d"%(Name,Marks))#Using % Formatting
#Important String Methods
text="Python"
print(text.upper())#Upper string
Message="HELLO EVERYONE"
print(Message.lower())#Lower String
Text="Python is a programming language"
print(Text.capitalize())#Capitalize string(first letter is capital)
Words="My name is Jiya Kumari"
print(Words.title())#Title String(first leter is capital of each words)
Word="I like python language"
print(Word.replace("like","love"))#Replace String
Texting="I learn a programmig"
print(Texting.find("learn"))#find string
print(Texting.split())#Split string(convert a string into list)
Name=" Jiya    Kumari "
print(Name.strip())#Strip string(remove extra space)
print(Name.startswith("ya"))#startswith string(string start with a given value)
Text="Python.py"
print(Text.endswith(".py"))#endswith string(string end with a given value)
text=="Hello everyone i am here "
print(len(text))#length string
print(text[5])
print(text[2:3])
print(text[-7:-3])