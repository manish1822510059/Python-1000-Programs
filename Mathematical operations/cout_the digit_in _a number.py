num = int(input("Enter a number :\t"))
count = 0
while(num>0):
    num = num//10
    count+=1

print("Total digits in the no is ",count)
    