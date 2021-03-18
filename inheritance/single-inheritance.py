class base:
    def cal_sum(self,a,b):
        return a+b

class Derived(base):
    def cal_mul(self,a,b):
        return a*b


n1= int(input("Enter the 1st no:"))     
n2= int(input("Enter the 2st no:"))                

d = Derived()
print("(from Base class) addition is:-",d.cal_sum(n1,n2))
print("(from Derived class) Multiplication is:-",d.cal_mul(n1,n2))