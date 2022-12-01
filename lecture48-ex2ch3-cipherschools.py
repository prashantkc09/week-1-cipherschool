#Exercise watch coco
#ask users name and age
name=input("Your name: ")
age=int(input("Your age: "))

#if users name start with ("a" or 'A') and age is above 10 then 
#he can watch coco else not
if (name[0]=='a' or name[0]=='A') and age>10:
    print("You can watch coco")
else:
    print("sorry you cannot watch coco")