# This program prompts the user to input a time in seconds
# then the program converts the seconds to days, hours,
# minutes, and seconds.

seconds = float(input('Enter the number of seconds: '))

# Calculations

day = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
seconds = seconds
print('%d Days: %d Hours: %d Minutes: %d Seconds' % (day, hour, minutes, seconds))
