# This program lets a user enter a course number
# the program then displays the course's room number,
# instructor, and meeting time.

def main():
    # Room dictionary
    rooms = {'CS101': '3004', 'CS102': '4501',
             'CS103': '6755', 'NT110': '1244',
             'CM241': '1411'}
    
    # Instructors dictionary
    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado',
                   'CS103': 'Rich', 'NT110': 'Burke',
                   'CM241': 'Lee'}

    # Class time dictionary
    time = {'CS101': '8:30 a.m.', 'CS102': '9:00 a.m.',
            'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.',
            'CM241': '1:00 p.m.'}

    # Get user input on course
    course = input('Enter a course number: ')
    if course in rooms:
        print('------------------------------')
        print()
        print('Room Number:', rooms[course])
        print('Instructor:', instructors[course])
        print('Course time:', time[course])
    else:
        print('Course not found')

# Call the main function
main()
