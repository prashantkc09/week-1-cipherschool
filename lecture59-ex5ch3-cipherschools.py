#ask a user for name 
#print count of charcter in name
name=input("enter your name: ")
y=""
i=0
while i<len(name):
    if name[i] not in  y:
        y=y+name[i]
        count=name.count(name[i])
        print(f"{name[i]} : {count}")
    i=i+1