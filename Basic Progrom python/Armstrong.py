n = int(input("Enter the number: \t"))
t = n
r = 0
while(n>0):
    a = n%10
    r = r +a*a*a
    n = n //10

if(r==t):
    print("Armstrong Number")
else:
    print("Not An Armstrong Number")        
