class Student:
    college_name = "ABC College"
    branch = "CSE"
    name = "Anonymous"  #class attr
    
    def __init__(self,name,marks):
        self.name=name  #obj attr 
        self.marks=marks
    
    def hello(self):
        print("hello",self.name)

s1 = Student("Deepanshu",94)
s2 = Student("Rohan",90)
s3 = Student("Mohit",80)

print(s1.name,s1.college_name,s1.branch,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)
s1.hello()

class School:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("hi", self.name ,"your avg score is:",sum/3)        
    

s1 = School("Deepanshu",[94,78,98])
s1.avg()