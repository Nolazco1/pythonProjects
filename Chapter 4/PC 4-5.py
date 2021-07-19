# This program prompts the user to enter
# a nonnegative integer then calculates
# its factorial number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get number
n = int(input("Enter a number to calculate the factiorial : "))
print(factorial(n))
