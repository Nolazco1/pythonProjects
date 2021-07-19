# This program accepts a string as an arguement
# and returns a copy of the string with the
# first character in each sentence capitalized.

def main():
    import re

    # Get sentence from user
    my_string = input("Enter text: ")
    cap = re.split('([.!?] *)', my_string)
    new = ''.join([i.capitalize() for i in cap])

    # Display result
    print(new)
        
# Call the main function    
main()
    
