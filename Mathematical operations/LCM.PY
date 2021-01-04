a = int(input("Enter the First no :\t"))
b = int(input("Enter the First no :\t"))
if(a>b):
    min = a
else:
    min = b    
while(1):
    if(min%a==0 and min%b==0):
        print("LCM is ",min)
        break
    min = min +1
        