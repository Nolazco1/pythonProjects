# This program creates the Employee class and
# ProductionWorker subclass
class Employee:
    # Data Attributes
    def __init(self, name, number):
        self.__name = name
        self.__employee_num = number

    # The class mutators
    def set_name(self, name):
        self.__name = name

    def set_employee_number(self, number):
        self.__employee_num = number

    # The class accessors

    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_num

class ShiftSupervisor(Employee):
    def __init__(self, name, number, salary, bonus):
        Employee.__init__(self, name, number)
        self.__salary = float(salary)
        self.__bonus = float(bonus)

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

def main():
    susan = ShiftSupervisor('Susan McDonald', 55834, 53500, 1200)

    print('Name:', susan.get_name())
    print('Employee Number:', susan.get_employee_number())
    print('Salary: $', susan.get_salary())
    print('Bonus: $', susan.get_bonus())

main()
