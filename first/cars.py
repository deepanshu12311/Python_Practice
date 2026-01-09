#This is an example of single inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stopped...")
#     color = "Black"

# class Toyota_car(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = Toyota_car("Fortuner")
# car2 = Toyota_car("Hyryder")

# print(car1.name)
# print(car1.color)
# car1.start()
# car1.stop()
# print(car2.name)
# print(car2.color)
# car2.start()
# car2.stop()

#This is an example of multi level inheritance

class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")
    color = "Black"

class Toyota_car(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota_car):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1 = Toyota_car("Toyota")
car1.start()
print(car1.type)