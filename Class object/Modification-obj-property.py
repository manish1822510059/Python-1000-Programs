class student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def show(self):
        print("Student Detail:") 
        print("NAME:",self.name)
        print("COURSE:",self.course)

s = student("Mohit","M.TECH")
s.show()  
s = student("Manish kumar","B.TECH")
s.show()      