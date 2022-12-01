#Sum of n natural numbers using while loop
n=int(input("Enter value of n: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(f"Sum of {n} natural numnbers is {sum}")