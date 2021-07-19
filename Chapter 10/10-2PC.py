# This program creates a Car class and asks the user
# for the year, make, and speed of the car. The program then
# displays its accelaration each time the class is called.

class Car:
    def __init__(self, year, make, speed):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    # Get the year
    def set_year_model(self, year):
        self.__year_model = year

    # Get the cars make
    def set_make(self, make):
        self.__make = make

    # Get the cars speed
    def set_speed(self, speed):
        self.__speed = 0

    # Display cars year
    def get_year_model(self):
        return self.__year_model

    # Display cars make
    def get_make(self):
        return self.__make

    # Display cars speed
    def get_speed(self):
        return self.__speed

    # Accelerate by 5
    def accelerate(self):
        self.__speed +=5

    # Brake by 5
    def brake(self):
        self.__speed -=5

    # Display the cars speed
    def get_speed(self):
        return self.__speed

def main():

    year = input('Enter the car year: ')
    make = input('Enter the car make: ')
    speed = 0

    mycar = Car(year, make, speed)

    # Accelerate 5 times
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed())
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed()) 

    # Brake 5 times
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake() 
    print('The current speed after brake is: ', mycar.get_speed())
    mycar.brake()
    print('The current speed after brake is: ', mycar.get_speed())

#Call the main function
main()
