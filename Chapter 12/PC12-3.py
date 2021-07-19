# This program accepts a list and then uses a recursive
# function to get the sum.

def main():
    # Number list
    numbers = [1, 3, 5, 7, 9, 11, 13]

    # Gets the sum of the list
    my_sum = range_sum(numbers, 0, 6)

    # Display the sum.
    print('The sum of the list is', my_sum)

# Calculates the sum of the list
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# Call the main function
main()
