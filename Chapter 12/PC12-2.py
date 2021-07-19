# This program uses recursion to find the largest
# value in a list.

# Calculates largest item
def largest_item(xs):
    if len(xs) == 1:
        return xs[0]
    elif xs[0] > xs[1]:
        xs.pop(1)
        return largest_item(xs)
    else:
        xs.pop(0)
        return largest_item(xs)

# The main function
def main():
    print(largest_item([5, 7, 9, 22, 33]))

# Call the main function
main()
