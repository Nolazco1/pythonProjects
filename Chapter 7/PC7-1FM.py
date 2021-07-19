# This program prompts the user to enter
# a stores sales for each day of the week
# and stores them in a list.

def main():
    # Constants
    total = 0
    sales = [0, 1, 2, 3, 4, 5, 6]
    index = 0

    # Defines list to days of the week.
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    for index in range(7):
        # Get sales for each day
        print('Enter store sales for', day_of_week[index])
        sales[index] = float(input('Enter the total sales for day: '))
        total += sales[index]

    # Displays total sales for the week.
    print('The total sales for the week is $', total)

# Call the main function
main()
    
