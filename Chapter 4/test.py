# This program predicts the population increase of
# organisms over a span of 10 days.

start_pop = int(input("Starting number of organisms: "))
increase = float(input("Average daily increase %: "))/100.0
days = int(input("Number of days to multiply: "))
first = True

# Chart of increase in population
print("Day\tApproximate Population")
for days in range(start_pop, days + 1):
    if first:
        print(1, '\t', start_pop)
        first = False
    add = start_pop * increase
    start_pop = start_pop + add
    print(days, '\t', format(start_pop, ',.2f'))
