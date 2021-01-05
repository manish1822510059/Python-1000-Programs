from math import sqrt
side = int(input("Enter length of sides:\t"))
area =(sqrt(5*(5+2*(sqrt(5))))*side*side)/4
print("Arae of pentagon : {0:2f}".format(area))