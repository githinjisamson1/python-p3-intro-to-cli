#!/usr/bin/env python3


def create_grade_report(student_grades):
    with open('lib/reports/grade_report.txt', 'w') as gr:
        for grade in student_grades:
            # add '\n' to write grades on separate lines
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        # end when no grade is entered
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)

# TODO: BEST PRACTICES IN CLI DESIGN
'''
Separate user input from functionality
A CLI depends on user input and a lot of code to act on it, but that doesn't mean it all has to be in the same place. As with any other Python program, your CLI should be grouped into classes and functions. Your scripted code- that is, the code inside of your if __name__ == '__main__' block- should only include user input and calls to classes and functions.


Validate user input
A good CLI will check the format of user input before using it to perform any actions. This can be carried out using regular expressions through the re module, the built-in type() and isinstance() functions, the various Python operators, and more.

Keep the end user informed
A CLI should always inform the end user of what it is doing and where to find output. This should always happen through the CLI itself, but it's often helpful to store the messages from a session in a logs directory as well.

Use external libraries to standardize your code
Two popular libraries that will help you make amazing CLIs are Click and Fire. While we won't require you to use these in your Phase 3 project, we strongly recommend that you use one. (It's another library to add to your resumé!)



'''