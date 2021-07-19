# This program calculates an items total including
# state sales tax, county sales tax, combined tax
# and sales total

state_sales_tax = .05
county_sales_tax = .025

# Get item price 
item_price = float(input('Enter the price of the item: $'))

# Calculations
state_tax = item_price * state_sales_tax
county_tax = item_price * county_sales_tax
total_tax = state_tax + county_tax
sales_total = item_price + total_tax

# Totals
print('State Tax: $', format(state_tax, '.2f'), sep='')
print('County Tax: $', format(county_tax, '.2f'), sep='')
print('Total Tax: $', format(total_tax, '.2f'), sep='')
print('Sale Total: $', format(sales_total, '.2f'), sep='')
