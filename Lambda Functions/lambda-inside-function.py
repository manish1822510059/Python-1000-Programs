def double(a):
    return lambda a:a*a*a

cal = double(10)
print("Result :",cal(4))