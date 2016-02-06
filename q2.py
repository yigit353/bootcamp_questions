'''
Take name and age from the user.
Ask for lecture name, lecturer name and letter grade. Continue until user decides otherwise (y/N).
Print the resulting dictionary in the end
'''

__author__ = 'Yigit Bekir Kaya <admin@cbilab.org>'

try:
    # Get name and age
    name = raw_input('Name: ')
    age = int(raw_input('Age: '))
    lectures = []

    while True:
        # Get lecture info
        lecture_name = raw_input('Lecture Name: ')
        lecturer_name = raw_input('Lecturer Name: ')
        letter_grade = raw_input('Letter Grade: ')
        
        # Append dictionary to lectures list
        lectures.append({
            'lecture_name': lecture_name,
            'lecturer_name': lecturer_name,
            'letter_grade': letter_grade
        })
        
        should_continue = True
        
        while True:
            # Ask for user input and continue asking until the answer is either y or N
            answer = raw_input('Do you want to continue (y/N)')
            
            # If answer is y continue
            if answer == 'y':
                break
            
            # Else if answer is N loop should not continue
            elif answer == 'N':
                should_continue = False
                break
            
            # If the choice is neither ask again
            else:
                continue
            
        # If the answer is y continue
        if should_continue:
            continue
        
        # If answer is not y, i.e. N break
        break
    
    # Create a dictionary consisting of user's name, age and list of the lectures as dictionaries
    print {
        'name': name,
        'age': age,
        'lectures': lectures
    }

# If any problem occurs while getting input report it
except Exception as e:
    print 'Something went wrong {0}'.format(e.message)
