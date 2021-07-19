# This program converts kilometers to
# miles.

def main():
    km = int(input("Enter the amount of kilometer's to convert: "))
    miles = km * 0.6214
    print('That is', format(miles, ',.2f'),'miles')

# Run the main function
main()
