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
# file=open("data.txt","r")
# print(file.read())
# file.close()

#2.Write Mode(w):-create a new file if it does not exist.if the file exists, all previous content is deleted.
file=open("data.txt","w")
file.write("Python language")
file.close()

#3.Append Mode(a):-Adds data at the end without deleting existing content.
file=open("data.txt","a")
file.write("\nJava")
file.close()

#4.Create Mode(x):-Create a new file
file=open("/Users/Jiya1/Downloads/Fun_ques%20(1).pdf ","x")
file.close()

##Read Methods:-
# 1.read(n):-reads the whole file.
file=open(" ","r")
print(file.read())
file.close()
#2.readline():-reads one line.
file=open(" ","r")
print(file.readline())
print(file.readline())
file.close()
#3.readlines():-reads all lines into a list.
file=open("","r")
print(file.readlines())
file.close()

##Write Methods:-
#1.write():-writes a string
file=open(" ","w")
file.write("python")
file.close()
#2.writelines():-writes multiple lines
file=open(" ","w")
lines=[
    "Apple\n",
    "Banana\n",
    "Orange"
]
file.writelines(lines)
file.close()

##Close():-always close the file
file.close()

##Using with open():-python automatically close the file.
with open(" ","r") as file:
    print(file.read())
#no need to call close().
# 
# #FILE POINTER:-keeps track of the current position in the file.
file=open("conditional.py ","r")
print(file.read(5))
print(file.read())
file.close()
#the pointer moves forward as data is read

##tell():-returns the current position of the file pointer.
    

