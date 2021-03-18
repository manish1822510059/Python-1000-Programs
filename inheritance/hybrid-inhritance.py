class Students:
    def getStudDetails(self):
        self.sName = input("Enter Student Name :")
        self.sRoll = input("Enter Student's Enroll NO :")

    def showStudDetails(self):
        print("\n STUDENT DETAILS")
        
        print("Student Name :",self.sName)    
        print("Student Enroll no, :",self.sRoll)

class Academics(Students):
    total = 0
    def getMarks(self):
        for x in range(5):
            print("Enter marks for subjects ",(x+1),":",end="")
            self.marks = int(input())
            self.total = self.total + self.marks

    def getATotal(self):
        self.showStudDetails() 
        return self.total



class Sports:
    spName = ""
    grade = 0
    
    def getSport(self):
        self.spName = input("Enter Sports Name :")
        self.grade = input("Enter Sports Marks :")


    def getSmarks(self):
        return self.grade

    def showSport(self):
        print("Sport Name :",self.spName)


class Results(Academics,Sports):
    def getResult(self):
        self.getStudDetails()
        self.getMarks()
        self.getSport()

    def showResult(self):
        aTotal = int(self.getATotal())
        sTotal = int(self.getSmarks())

        per =(aTotal+sTotal)/6
        print("Percentage: {:.2f} ".format(per))
        self.showSport()


r = Results()
r.getResult()
r.showResult()        
