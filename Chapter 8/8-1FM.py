# This program displays the sum of all the
# single digit numbers in a string.

def main():
    string = input('Enter a series of numbers without spaces and I will add them.\n')
                      
    total = 0

    for num in string:
        total += int(num)

    print('The sum of the digits in', string, 'is', str(total) + '.')

# Call the main function
main()
