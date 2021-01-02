n = int(input("Enter the no: \t"))

sum = 0
while(n>0):
    x=n%10
    sum = sum+x
    n = n//10

print("Sum of digits of the numbers",sum)    