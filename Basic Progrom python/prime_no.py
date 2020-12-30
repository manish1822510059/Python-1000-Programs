count = 0
n = int(input("Enter the no : \t"))
for i in range(1,n+1):
    if n%i ==0:
       count+=1

if count==2:
    print(n,"is a prime number")
else:
    print(n,"is a non-prime number")    