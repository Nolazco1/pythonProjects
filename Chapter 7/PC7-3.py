# This program accepts two arguements a list
# and a number. It then displays all of the numbers
# in the list that are greater than n.

# Constants
list1 = [8, 6, 7, 5, 4, 1, 2, 9]
n = 3
index = 0

def main():
    # Display number list
    print('The list of numbers are', list1)
    
    for index in list1:
        # Determines if number in list is greater than n
        print('Is', index, 'greater than n(3)?', index >= 3)

# Call the main function
main()
