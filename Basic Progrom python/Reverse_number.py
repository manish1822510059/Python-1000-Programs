n  = int(input("Eneter a number to reverse: \t"))

rev = 0
while(n!=0):
    rev=rev*10
    rev=rev+n%10
    n=n//10

print("Reverse of Entered Number is ",rev)