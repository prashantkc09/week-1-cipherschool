#ask user to input 3 numbers and you have to print average of 3 numbbers using string formatting
#bonus:-try to take all the 3 comma seperated inputs in one line
num1,num2,num3=input("enter number seperated by commas: ").split(",")
print(f"average of three numbers : {(int(num1) + int(num2) + int(num3))/3}")
