# This program creates an object of the pet class
# and asks the user to enter the name, type, and age of pet.
# The program retrieves the pet's name, type, and age and
# displays the data.

class Pet:
    def __init__(self, name, animal_type, age):
        # Gets the pets name
        self.__name = name
        # Gets the animal type
        self.__animal_type = animal_type
        # Gets the animals age
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Displays the pets name
    def get_name(self):
        return self.__name

    # Displays the animal type
    def get_animal_type(self):
        return self.__animal_type

    # Displays the pets age
    def get_age(self):
        return self.__age

# The main function
def main():
    # Get the pets name
    name = input('What is the name of the pet? ')
    # Get the animal type
    animal_type = input('What type of animal is it? ')
    # Get the animals age
    age = int(input('How old is the pet? '))

    pets = Pet(name, animal_type, age)

    # Display the inputs
    print('This information will be added to our records.')
    print('Here is the data you entered: ')
    print('------------------------------')
    print('Pet Name:', pets.get_name())
    print('Animal Type:', pets.get_animal_type())
    print('Age:', pets.get_age())

# Call the main function
main()
