s1 = input("Enter the string to check palindrome: \t")
s2 = " "
for i in s1:
    print(s1)
    s2  = i+s2
if(s1==s2):
    print("Yes it is palindrome")  
else:
    print("Yes, it is not palindrome")      