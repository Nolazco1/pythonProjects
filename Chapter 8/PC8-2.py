# This program asks the user to enter a 10
# character telephone number in the format
# XXX-XXX-XXXX. It then displays the telephone
# number with any alphabetic characters that appeared
# in the original translated to their numeric equivalent.

def main():
    # Get a telephone number
    phone_number = input('Enter a telephone number in the format 555-XXX-XXXX: ')
    new_number = ''

    for char in phone_number:
        if char == 'A' or char == 'B' or char == 'C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'
                    
        new_number = new_number + char

    # Display results
    print(new_number)

# Call the main function
main()
    
