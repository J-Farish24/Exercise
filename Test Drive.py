#Import class
import CarClass as c

#Ask user for car information
year = int(input("Enter your car's year model: "))
make = input("Enter your car's make: ")
#Create test car object
test_car = c.Car(year,make)
#Car accelerates five times
print('Time to accelerate!')
for count in range(5):
    test_car.accelerate()
    print(test_car.get_speed())
#Car brakes five times
print('Time to slow down!')
for count in range(5):
    test_car.brake()
    print(test_car.get_speed())

