from functools import reduce
num = [1,2,3,4,5]
prod = reduce(lambda x,y:x*y,num)
print("Produced of all numbers in the list:",prod)