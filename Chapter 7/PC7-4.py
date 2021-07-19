# This program determines if a two-dimensional list is
# a Lo Shu Magic Square.

# Two-dimensional list properties
rows = 3
columns = 3

def main():
    # List input
    magic_square = [[8, 1, 6],[3, 5, 7],[4, 9, 2]]

    # Determines if it's a Lo Shu Magic Square
    for row in magic_square:
        for i in range (columns):
            if sum(row) == sum (magic_square[i][i] for i in range(columns)):
                if sum(row)== sum(row[i] for row in magic_square):
                    answer = str('a Lo Shu Magic Square')
            else:
                answer = str('not a Lo Shu Magic Square')

    # Results
    print("The list is", answer)

# Call the main function
main()
