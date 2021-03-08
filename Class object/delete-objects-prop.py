class Student:
    def __init__(self,name,course,sex):
        self.name = name
        self.course = course
        self.sex = sex

s = Student("Mohit","Mtech","Male") 
print("Student Detail:")
print("NAME:",s.name)
print("COURSE",s.course)
print("SEX",s.sex)

#deleting sex
del s.sex
print("Student Detail:")
print("NAME:",s.name)
print("COURSE",s.course)
# print("SEX",s.sex)