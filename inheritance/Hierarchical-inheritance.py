class Base:
    a = 10
    b = 20


class DerivedA(Base):
    def sum(self):
        add = self.a+self.b
        print("Addition is ", add)


class DerivedB(Base):
     def mul(self):
        mul = self.a*self.b
        print("Product is ",mul)


dA = DerivedA()
dB = DerivedB()

dA.sum()
dB.mul()


