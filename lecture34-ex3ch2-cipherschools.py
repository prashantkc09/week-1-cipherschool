#take 2 comma seperated inputs from user
#1.name and 2.single character
#print 1.name length and num of single character in name
name,char=input("Enter name and char sep by commas: ").split(",")
print(len(name))
name,char=name.lower(),char.lower()
print(name.count(char))