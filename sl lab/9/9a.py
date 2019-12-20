class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def getvalue(self):
        self.name=input("Enter the name")
        self.age=int(input("Enter the age"))
        for i in range(3):
            self.marks.append(int(input("Enter the marks")))
    def displayval(self):
        print(self.name," ",self.age," ",self.marks)
i=student("","",[])
i.getvalue()
i.displayval()