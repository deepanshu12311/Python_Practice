# class student:
#     Name = "Karan Johar"
#     Age = 21
#     Gender = "Not Defined"
    
# s1 = student()
# print(s1.Name)
# print(s1.Gender)
# print(s1.Age)
class student:
    
    #Default constructors
    def __init__(self):
        pass
    
    #Parameterized conductors
    def __init__(self,fullname):
        self.name=fullname
        
        
s1= student("Deepanshu")
s2= student("Mohit")

print(s1.name)
print(s2.name)
 
class animal:
    def __init__(self,name_of_animal,power):
        self.name=name_of_animal
        self.power=power

a = animal("Bull",100)
b = animal("Ship",150)
c = animal("Hen",10)
d = animal("cow",200)

print(a.name)
print(a.power)