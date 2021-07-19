# This program solves Ackermann's function

# Ackermann's function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# The main function
def main():
    print(ackermann(2, 5))

# Call the main function
main()
