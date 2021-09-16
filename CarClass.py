#Create Car class
class Car:
    #Initialize object attributes
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return str(self.__speed) + ' MPH' 
    
