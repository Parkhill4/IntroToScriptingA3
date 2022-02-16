"""
        Question 1: This program creates a car class and will use an object to
                    call the accelerate and brake members to increase and decrease
                    the speed variable
"""

#Creating the class car that will initialize 3 members
class Car():
    def __init__(self, make, year_model):
        self.__make = make
        self.__year_model = year_model
        self.__speed = 0
#This function will increase variable speed by 5
    def accelerate(self):
        self.__speed += 5
#This function will decrease variable speed by 5
    def brake(self):
        self.__speed -= 5
#Return the speed value
    def get_speed(self):
        return self.__speed
#Return the make of the car
    def get_make(self):
        return self.__make
#Return the year and model of the car
    def get_year_model(self):
        return self.__year_model
#Printing the make year and model
my_car = Car("Hyundai", "Kona 2020")
print(my_car.get_make(), my_car.get_year_model())
#Using the accelerate and brake functions in loops will call them multiple times
#to change the speed value
for i in range(5):
    my_car.accelerate()
    print(my_car.get_speed())
for i in range(5):
    my_car.brake()
    print(my_car.get_speed())
