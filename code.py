items={
    "home":"Decorative items",
    "Furniture":"Table",
    "vegetable":"carrot"
}
# print(len(items))#length of items
student=dict(name="Jiya",
             age=19,
             height=5.1)
print(student)#using constructor
print(type(student))#type method
num=[("a",1),("b",2),("c",3)]
d=dict(num)
print(d)#tuple convert into dict
Data=[("lang","Python"),      
      ("num",12),
      ("price",23.4),
      ("status",True)]
d=dict(Data)
print(d)

#Accessing dict value
#using square brackets
student={
    "name":"jiya",
    "city":"mahendergarh",
    "age":19
}
print(student["age"])
#if the key does not exist,this gies error
#using get():you can also use get method to access dict items
print(student.get("email"))
print(student.get("name"))
#we can also provides a default values
print(student.get("email","email not available"))

#adding and updating dict items
#adding a key value pair
student={
    "name":"Jiya",
    "course":"AI engineering",
    "age":19
}
student["city"]="Delhi"
print(student)#adding new element
#updating an existing value
student["age"]=22
print(student)

#using update ()
student.update({
    "course":"python",
    "city":"Mumbai"
})
print(student)

#Removing items from a dict
#using pop()
student={
     "name":"Subham",
     "age":21,
     "course":"python"

}
a=student.pop(
    "course","python"
)

print(a)
print(student)
a=student.popitem()
#using del keyword removes the item with the specified key name:
student={
    "name","jiya",
    "city","mumbai"
}
print(student.clear())#clear method
#dict are useful for storing student records
#storing employeee details

