import random

num = int(input("Enter the number of random  no. you want: \t"))
max = int(input("Enter the maximum value of randam no:\t"))
print(num,"random number between 0 to",max)
for i in range(num):
    print(random.randint(0,max))