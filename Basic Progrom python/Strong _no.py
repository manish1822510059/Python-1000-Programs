num = int(input("Enter the number: \t"))
t = num
sum = 0

while(num):
    i = 1
    p = 1
    r = num%10
    while(i<=r):
        p=p*i
        i+=1
    sum  = sum+p
    num = num//10

if(sum==t):
    print(t,"is a Strong Number")
else:
    print(t,"is not a Strong Number")    