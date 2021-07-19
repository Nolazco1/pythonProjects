# This program asks the user to enter
# five test scores. The program should
# display a letter grade for each score
# and the average test scores.

# Get test scores
def main():
    grade1 = float(input("Enter test score 1: "))
    grade2 = float(input("Enter test score 2: "))
    grade3 = float(input("Enter test score 3: "))
    grade4 = float(input("Enter test score 4: "))
    grade5 = float(input("Enter test score 5: "))
    show_scores(grade1, grade2, grade3, grade4, grade5)
    calc_average(grade1, grade2, grade3, grade4, grade5)

# Display results
def show_scores(grade1, grade2, grade3, grade4, grade5):
    print("{} is {}".format(grade1, determine_grade(grade1)))
    print("{} is {}".format(grade2, determine_grade(grade2)))
    print("{} is {}".format(grade3, determine_grade(grade3)))
    print("{} is {}".format(grade4, determine_grade(grade4)))
    print("{} is {}".format(grade5, determine_grade(grade5)))

# Determine letter grade
def determine_grade(grade):
    if (grade < 60):
        determine_grade = "F"
    elif (grade < 70):
        determine_grade ="D"
    elif (grade < 80):
        determine_grade = "C"
    elif (grade < 90):
        determine_grade = "B"
    elif (grade < 101):
        determine_grade = "A"
    return determine_grade

# Calculate average
def calc_average(grade1, grade2, grade3, grade4, grade5):
    average = (grade1 + grade2 + grade3 + grade4 + grade5)/ 5
    print("The average is {}".format(average))

# Run main function
main()
    
    
    
    
