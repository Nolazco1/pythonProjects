# This program is a recursive function that accepts
# an interger n, and prints the number 1 through n.

def main():
    num = int(input('Enter a number to count to: '))
    recfun(num)

def recfun(num):
    if num == 1:
        print(num)
    else:
        recfun(num - 1)
        print(num)

# Call the main function
main()
