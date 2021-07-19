# This program displays expenses of last month
# and generates them into a pie chart.
import matplotlib.pyplot as plt

def main():
    # Provide data for file
    expense = ["800", "80", "200", "60", "260", "120"]
    category = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]
    # Open the file
    f = open("expense.txt", "r+")
    
    # Write the data onto file
    f.writelines(category)
    f.writelines(expense)

    # Read data
    f.readlines()
    f.readlines()

    # Create the pie chart
    plt.pie (expense, labels = category)
    plt.title ("Last Month's Expenses")

    # Show the pie chart
    plt.show()

    # Close the file
    f.close ()

# Call the main function
main()
                          
                
              
    
