# This program calculates and displays the
# total travel expenses of a business person
# on a trip.
        
def main():
    print('Calculate Total Cost of a Business Trip per person.')
    print('------------------------------------------------------')
    # Call the input functions for trip
    days = totalDays()
    departure = departureTime()    
    arrival = arrivalTime()
    airfare = airfareAmount()
    rental = carRental()
    privateExpense = privateVehicle()
    parking = parkingFee()
    taxi = taxiFee()
    regis = registrationFee()
    hotel = hotelAmount()

    # Get meal costs and allowances
    if departure < '07:00':
        firstMeal = breakfast1()
    elif departure < '12:00':
        firstMeal = lunch1()
    elif departure < '18:00':
        firstMeal = dinner1()

    if arrival < '07:00':
        secondMeal = breakfast2()
    elif arrival < '12:00':
        secondMeal = lunch2()
    elif arrival < '18:00':
        secondMeal = dinner2()

    

    # Total cost of trip
    total = (airfare)+(rental)+(privateExpense)+(parking)+(taxi)\
            +(regis)+(hotel)+(firstMeal)+(secondMeal)
            
    print('------------------------------------------------------')
    print('A total of $', format(total, '.2f'), ' was spent.', sep='')
    print('------------------------------------------------------')

    # Costs owed back to the company header
    print('Here is the total expenses that are owed.')
    print('------------------------------------------------------')

    # Parking cost owed
    parking_allowed = 6.00 * days
    pOwed = parking - parking_allowed
    if pOwed <= 0.00:
        print("You don't owe any parking fees.")
    else:
        print('You owe $', format(pOwed,'.2f'), ' in parking fees.', sep='')

    # Taxi cost owed
    taxi_allowed = 10.00 * days
    tOwed = taxi - taxi_allowed
    if tOwed <= 0.00:
        print("You don't owe any taxi fees.")
    else:
        print('You owe $', format(tOwed,'.2f'), ' in taxi fees.', sep='')

    # Hotel cost owed
    hotel_allowed = 90.00 * (days - 1)
    hOwed = hotel - hotel_allowed
    if hOwed <= 0.00:
        print("You don't owe any hotel fees.")
    else:
        print('You owe $', format(hOwed,'.2f'), ' in hotel fees.', sep='')

    # First meal cost owed
    print('You owe $', format(firstMeal,'.2f'), ' on the first meal.', sep='')

    # Second meal cost owed
    print('You owe $', format(secondMeal,'.2f'), ' on the first meal.', sep='')

    # Total owed
    totalOwed = pOwed + tOwed + hOwed + firstMeal + secondMeal
    print('You owe a total of $', format(totalOwed,'-.2f'), ' in fees.', sep='')

    # Total company is covering
    covered = total - totalOwed
    if totalOwed <= 0.00:
        totalOwed = 0
    print('The company will cover $', format(covered,'.2f'), sep='')
    
    
def totalDays():
    print('Please enter all times in military format (HH:MM).')
    input('Press Enter to continue. ')
    # Get total days spent on trip
    days = int(input('How many days were spent on the trip? '))
    while days <= 1:
        print('Error: Values at or under 1 are not accepted.')
        print('Please enter a valid number of days. ')
        days = int(input('How many days were spent on the trip? '))
    return days

def departureTime():
    import datetime
    # Get departure time
    valid = False
    while not valid:
        departure = input('What was the departure time on first day(HH:MM)? ')
        try:
            departure_time = datetime.datetime.strptime(departure, '%H:%M')
            valid = True
        except:
             print('Error: Use military time(HH:MM).')
    return departure

def arrivalTime():
    import datetime
    # Get arrival time
    valid = False
    while not valid:
        arrival = input('What was the arrival time on last day(HH:MM)? ')
        try:
            arrival_time = datetime.datetime.strptime(arrival, '%H:%M')
            valid = True
        except:
            print('Error: Use military time(HH:MM).')
    return arrival

def airfareAmount():
    # Get airfare cost
    airfare = float(input('What was the airfare cost? '))
    return airfare

def carRental():
    # Get car rental cost
    rental = float(input('What was the car rental cost? '))
    return rental

def privateVehicle():
    # Ask if private vehicle was used
    private = input('Was a private vehicle used? Y = Yes N = No: ')

    if private == 'y':
        miles = float(input('How many miles were driven? '))
        privateExpense = miles * 0.27
        return privateExpense
    else:
        privateExpense = 0
        return privateExpense
        print('No private vehicle input received.')
        
def parkingFee():
    # Get parking fees
    parking = float(input('How much was spent on parking fees? '))
    return parking

def taxiFee():
    # Get taxi fees
    taxi = float(input('How much was spent on taxi fees? '))
    return taxi

def registrationFee():
    # Get registration fees
    regis = float(input('How much was spent on registration fees? '))
    return regis

def hotelAmount():
    # Get hotel cost
    hotel = float(input('How much was spent on the hotel? '))
    return hotel

def breakfast1():
    # Get first breakfast cost
    breakfast_allowance = 9.00
    breakfast = input('Was breakfast eaten on 1st day? Y = Yes N = No: ')
    if breakfast == 'y':
        breakfast1Fee = float(input('How much was spent on breakfast? '))
        breakfast1Owed = breakfast1Fee - breakfast_allowance
        if breakfast1Owed <= 0.00:
            breakfast1Owed = 0
            return breakfast1Owed
        else:
            return breakfast1Owed

def lunch1():
    # Get first lunch cost
    lunch_allowance = 12.00
    lunch = input('Was lunch eaten on 1st day? Y = Yes N = No: ')
    if lunch == 'y':
        lunch1Fee = float(input('How much was spent on lunch? '))
        lunch1Owed = lunch1Fee - lunch_allowance
        if lunch1Owed <= 0.0:
            lunch1Owed = 0
            return lunch1Owed
    else:
        return lunch1Owed

def dinner1():
    # Get first dinner cost
    dinner_allowance = 16.00
    dinner = input('Was dinner eaten on 1st day? Y = Yes N = No: ')
    if dinner == 'y':
        dinner1Fee = float(input('How much was spent on dinner? '))
        dinner1Owed = dinner1Fee - dinner_allowance
        if dinner1Owed <= 0.0:
            dinner1Owed = 0
            return dinner1Owed
    else:
        return dinner1Owed

def breakfast2():
    # Get last breakfast cost
    breakfast_allowance = 9.00
    breakfast = input('Was breakfast eaten on last day? Y = Yes N = No: ')
    if breakfast == 'y':
        breakfast2Fee = float(input('How much was spent on breakfast? '))
        breakfast2Owed = breakfast2Fee - breakfast_allowance
        if breakfast2Owed <= 0.00:
            breakfast2Owed = 0
            return breakfast2Owed
        else:
            return breakfast2Owed

def lunch2():
    # Get last lunch cost
    lunch_allowance = 12.00
    lunch = input('Was lunch eaten on last day? Y = Yes N = No: ')
    if lunch == 'y':
        lunch2Fee = float(input('How much was spent on lunch? '))
        lunch2Owed = lunch2Fee - lunch_allowance
        if lunch2Owed <= 0.0:
            lunch2Owed = 0
            return lunch2Owed
    else:
        return lunch2Owed

def dinner2():
    # Get last dinner cost
    dinner_allowance = 16.00
    dinner = input('Was dinner eaten on last day? Y = Yes N = No: ')
    if dinner == 'y':
        dinner2Fee = float(input('How much was spent on dinner? '))
        dinner2Owed = dinner2Fee - dinner_allowance
        if dinner2Owed <= 0.0:
            dinner2Owed = 0
            return dinner2Owed
    else:
        return dinner2Owed
           
# Call the main function                                   
main()
