class student:
    @staticmethod  #decorator
    def college():
        print("Hello my friends")

student.college()

class car:
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car started..")

car1 = car()
car1.start()