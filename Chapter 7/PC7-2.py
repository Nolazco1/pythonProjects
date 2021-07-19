# This program asks the user to enter 20 different
# numbers and stores them in a list. It then displays
# the lowest num, highest num, total, and average of the numbers.

def main():
    # Defines constants
    numbers1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    numbers3 = numbers1 + numbers2
    index = 0
    total = 0
    
    # Get numbers
    for index in range(20):
        numbers3[index] = float(input('Enter a number: '))

    # Total value of numbers input
    for value in numbers3:
        total += value

    # Average value of numbers input
    average = total/len(numbers3)

    # Displays results
    print('The lowest number in the list is:', min(numbers3))
    print('The highest number in the list is:', max(numbers3))
    print('The total of the numbers in the list is:', total)
    print('The average of the numbers in the list is:', average)

        
# Call the main function
main()

    
