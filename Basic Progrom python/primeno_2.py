x = 2
ch = 0
n = int(input("enter the no: \t"))
#check for 1
if n<=1:
    ch=1
while x<=n/2:
    if n%x==0:
        ch=1
        break
    else:
        x+=1

if ch==0:
    print(n,"is a prime number")
else:
    print(n,"is a non-prime number")    