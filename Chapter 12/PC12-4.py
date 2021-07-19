# This program uses recursion to raise a number to
# a power. The function accepts two arguments, the number
# to be raised and the exponent.

# Calculates the power a number needs to be raised to
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# The main function
def main():
    print(power(4, 6))

# Call the main function
main()
