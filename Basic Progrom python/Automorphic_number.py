n = int(input("Enter the Number : \t"))
num = n
sq = n*n
t = 10
equal = False
print("Square of",n,"is",sq)
while(n>0):
    r=sq%t
    if(num==r):
        equal=True
        break
    n=n//10
    t=t*10


if(equal):
    print(num,"is an Automorphic Number")
else:
     print(num,"is Not an Automorphic Number")    
        
