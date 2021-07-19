# This program shows the rising of ocean
# level by 1.6mm per year over the next 25
# years.

print('Year\tSea Level Rise')
print('--------------------')
for year in range(1, 26):
    searise = year * 1.6
    print(year, '\t', format(searise, ',.2f'))
