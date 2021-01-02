n = int(input("Enter a number: \t"))
print("list of prime number between 1 to",n)
for i in range(1,n+1):
    cn = i #current no
    count =0
    for j in range(1,cn+1):
        if cn%j==0:
            count+=1
    if count==2:
        print(cn)      
