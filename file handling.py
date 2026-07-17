##FILE HANDLING IN PYTHON:-it is used to create,read,write,update,and delete files
#it allows to store data permanently instead of losing it when the program ends.
##FILE:-collection of data stored on a computer.
###WHY FILE HANNDLING:-
#@.WITHOUT FILE HANDLING:-1.Data is stored in RAM.
#With file handling:-Data is permanently saved
#2.you can access it anytime.
##Steps of file handling:-open file->read/write data->closed file
##SYNTAX:-file=open("filename","mode")
#Example:-file=open("data.txt","r")
##file modes:-
#1.READ MODE(r):-reads an existing file.
# file=open("loop.py","r")
# print(file.read())
# file.close()

# #2.Write Mode(w):-create a new file if it does not exist.if the file exists, all previous content is deleted.
# file=open("loop.py","w")
# file.write("Python language")
# file.close()

# #3.Append Mode(a):-Adds data at the end without deleting existing content.
file=open("fruits.txt","a")
file.write("\nJava")
file.close()
##append mode is useful for:-
#log file
#transaction historices
#attendance records
#activity records
#audit traits


# #4.Create Mode(x):-Create a new file
# file=open("conditional.py ","x")
# file.close()
# with open("output.txt","x") as file:
#   file.write("this is a new file")

# ##Read Methods:-
# # 1.read(n):-reads the whole file.
# file=open("loop2.py ","r")
# print(file.read())
# file.close()
#2.readline():-reads one line.
file=open("loop2.py ","r")
print(file.readline())
print(file.readline())
with open("operators.py","r") as file:
    first_line=file.readline()
    second_line=file.readline()
print(first_line)
print(second_line)    
# file.close()
# #3.readlines():-reads all lines into a list.
# file=open("conditional.py","r")
# print(file.readlines())
# file.close()
with open("operators.py","r") as file:
 lines=file.readlines()
print(lines)

##count 
line_count=0
with open("conditional.py","r") as file:
   for line in file:
    line_count +=1
print("number of lines:",line_count)    

##counting words and characters
with open("conditional.py","r") as file:
  content=file.read()
character_count=len(content)
word_count=len(content.split())  
line_count=len(content.split())

# ##Write Methods:-
# #1.write():-writes a string
# file=open("conditional.py ","w")
# file.write("python")
# file.close()
#2.writelines():-writes multiple lines
# file=open("data.py","w")
# print("table of fruits")
# lines=[
#     "Apple\n",
#     "Banana\n",
#     "Orange"
# ]
# print("table of fruits")
# file.writelines(lines)
# file.close()

#a more flexible alternative are
fruits=["apple","banana","mango"]
with open("fruits.txt","w") as file:
  for fruit in fruits:
    file.write(f"{fruit}\n")

# ##Close():-always close the file
# file.close()

# ##Using with open():-python automatically close the file.
# with open(" conditional.py","r") as file:
#     print(file.read())
# #no need to call close().
# # 
# # #FILE POINTER:-keeps track of the current position in the file.
# file=open("conditional.py ","r")
# print(file.read(5))
# print(file.read())
# file.close()
# #the pointer moves forward as data is read
with open("conditional.py","r") as file:
  print(file.read(5))
  print(file.read())

# ##tell():-returns the current position of the file pointer.
with open("loop2.py","r") as file:
  print(file.tell())    

#seek():changing the position,changes the current file position
with open("loop.py","r") as file:
  first_read=file.read()
  print(first_read)
  file.seek(1)
  second_read=file.read(10)
  print(second_read)
