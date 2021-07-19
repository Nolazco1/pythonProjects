# This programs ask how many tickets for
# each class of seats were sold, then displays
# the amount of income from ticket sales.

def main():
    # Get Class A seats
    a = int(input('How many Class A seats were sold? '))
    # Get Class B seats
    b = int(input('How many Class B seats were sold? '))
    # Get Class C Seats
    c = int(input('How many Class C seats were sold? '))
    total = (20 * a) + (15 * b) + (10 * c)
    # Show total income generated
    print('Your total income from sales was $',total, sep='')

# Run main functions   
main()
    
     
