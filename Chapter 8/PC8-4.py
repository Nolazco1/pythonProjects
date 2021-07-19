# This program lets the user enter a string and
# displays the character that appears most in the string.

def main():
    # Get string from user
    my_string = input('Enter a string: ')
    new_string = my_string.lower()

    # Variables
    count = 0
    total_count = 0

    appears_most = ''

    # Calculates most appeared character and counter
    for ch in my_string:
        for str in my_string:
            if str == ch:

                count += 1
        if count > total_count:
            total_count = count
            appears_most = ch
        count = 0

    # Displays result
    print('The most appeared character is', appears_most, 'and it appears', total_count, 'times.')

# Call main function
main()
