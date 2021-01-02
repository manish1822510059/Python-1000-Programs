num = int(input("Enter the number: \t"))
sq = num*num

sum = 0
while(sq>0):
    sum = sum+sq%10
    sq = sq//10


if(sum==num):
    print(num,"is a Neon Number")
else:
    print(num,"is not a Neon Number") 
       
