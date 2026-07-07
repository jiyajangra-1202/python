Num="100" # Numerical data types
print(Num)
x=float(Num)
y=int(Num)
z=complex(Num)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#string data types
a="hello  world"
print(len(a))
print(a[4])
print(a[2:11])

#methods for finding spcific word
message="""we are learning python and python is a great programming language
"""
print(len(message))
print("awesome"in message)
print("great"in message)
if "python" in message:
    print("true")
    print(message[3:8])
    print(message[-12:-2])#negative
    print(message[-14:-4])
    print(message[0:10])
    print(message[:10])
    print(message[12:])
    print(message.upper())#capital letters
    print(message.lower())#smaller letter
    print(message.replace('great','awesome'))#replace
    print(message.split())#spilt(gap removed)