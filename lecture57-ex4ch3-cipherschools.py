#calculate sum of digits of number using while loop
#Example input is 1256 then sum is 1+2+5+6
num=input("Enter a 2 or more digit number: ")
sum=0
i=0
while i<len(num):
    sum=sum+int(num[i])
    i=i+1
print(f"sum of digits of {num} is {sum}")