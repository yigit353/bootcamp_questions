'''
Take name and age from the user.
Ask for lecture name, lecturer name and letter grade. Continue until user decides otherwise (y/N).
Print the resulting dictionary in the end
'''

__author__ = 'Yigit Bekir Kaya <admin@cbilab.org>'

try:
    name = raw_input('Name: ')
    age = int(raw_input('Age: '))
    lectures = []

    while True:
        lecture_name = raw_input('Lecture Name: ')
        lecturer_name = raw_input('Lecturer Name: ')
        letter_grade = raw_input('Letter Grade: ')
        lectures.append({
            'lecture_name': lecture_name,
            'lecturer_name': lecturer_name,
            'letter_grade': letter_grade
        })
        should_continue = True
        while True:
            answer = raw_input('Do you want to continue (y/N)')
            if answer == 'y':
                break
            elif answer == 'N':
                should_continue = False
                break
            else:
                continue
        if should_continue:
            continue
        break
    print {
        'name': name,
        'age': age,
        'lectures': lectures
    }

except Exception as e:
    print 'Something went wrong {0}'.format(e.message)