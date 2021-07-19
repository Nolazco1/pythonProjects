# This program creates a Person class and then a Customer subclass.
# The program then provides a simple sample of the class.
class Person:
    # Class Attributes
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__addr = address
        self.__phone = phone_number

    # Class mutators
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__addr = address

    def set_phone_number(self, phone_number):
        self.__phone = phone_number

    # Class accessors
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__addr

    def get_phone_number(self):
        return self.__phone

# Customer subclass
class Customer(Person):
    # Class attributes
    def __init__(self, name, address, phone_number, customer_num, send_mail):
        self.__cust_num = customer_num
        self.__mail = send_mail
        Person.__init__(self, name, address, phone_number)

    # Class mutators
    def set_customer_number(self, customer_num):
        self.__cust_num = customer_num

    def set_mail_status(self, send_mail):
        self.__mail = send_mail

    # Class accessors
    def get_customer_number(self):
        return self.__cust_num

    def get_mail_status(self):
        return self.__mail

    # Returns the state of the object from __str__
    def __str__(self):
        if self.__mail == True:
            choice = 'On mailing list.'
        else:
            choice = 'Not on mailing list.'
        return 'Name: ' + self._Person__name + \
               '\nAddress: ' + self._Person__addr + \
               '\nPhone Number: ' + self._Person__phone + \
               '\nCustomer Number: ' + str(self.__cust_num) + \
               '\nMailing List? ' + choice

def main():
    robert = Customer('Robert Miranda', '553 W 3050 N Ogden, UT 84414', '801-398-3939', \
                      55321, True)

    print(robert)

main()
    
    
