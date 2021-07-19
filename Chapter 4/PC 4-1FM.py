# This program predicts the population of organisms
# over a span of 10 days.

start_pop = int(input('Starting number of organisms: '))
increase = float(input('Average daily increase %: '))/100
days = int(input('Number of days to multiply: '))

# Chart of increase in population
print('Days\tApproximate Population')
for days in range(1, days + 1):
    add = start_pop * increase
    start_pop = start_pop + add
    print(days, '\t', format(start_pop, ',.2f'))
