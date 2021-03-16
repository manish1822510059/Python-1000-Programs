
#for normal argumet like no list use *args
def result(*args):
    result = 0
    for i in args:
        result += i
    return result



result=result(12,45,78,89) 
print(result)     
