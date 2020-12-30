str = input("Enter the string to check palindrome: \t")
str = str.casefold()  #for caseless compare
if (str == str[::-1]):
    print("Yes, it is Palidrome")
else:
    print("NO, it is Palidrome")    