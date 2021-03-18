class University:
    def getUdetails(self):
        self.uName = input("Enter the University Name :")
        self.uRID = input("Enter The REG (University) No :")

    def showUdetails(self):
        print("University Name :", self.uName)
        print("University Reg No :", self.uRID)


class College(University):
    def getClgDetails(self):
        self.cName = input("Enter the College Name :")
        self.cRId = input("Enter Reg (College) No :")
        self.getUdetail()

    def showClgDetails(self):
        print("College Name:", self.cName)
        print("College Reg No :", self.cRId)
        self.showUdetails()


class Student(College):
    def getStudDetails(self):
        self.uName = input("Enter Student Name: ")
        self.sRoll = input("Enter Student's Enroll No:")
        self.sBranch = input("Enter Student Branch :")
        self.getClgDetails()

    def showStudDetails(self):
        print("\nSTUDENTS  DETAILS")
        print("Student Name :", self.sName)
        print("Student Rollno :", self.sRoll)
        print("Student Branch :", self.sBranch)
        self.showClgDetails()


s = Student()
s.getStudDetails()
s.showStudDetails()
