# Ulices Guzman
#M02.py
#This app is desgined to take studnet's name and GPA and determine if they have made the Dean's list or Honor Roll.

last_name = input("Please enter your last name or 'ZZZ' to quit: ")
while last_name != 'ZZZ':
    first_name = input("Please enter your first name: ")

    GPA = float(input("Please enter your GPA: "))
    if GPA >= 3.5:
        print("Congratulations! " + first_name + " " + last_name + ", you have made the Dean's list!")
        last_name = input("Please enter your last name or 'ZZZ' to quit: ")
    elif GPA < 3.5 and GPA >= 3.25:
        print("Congratulations! " + first_name + " " + last_name + ", you have made the Honor Roll!")
        last_name = input("Please enter your last name or 'ZZZ' to quit: ")
    else:
        print("Sorry, " + first_name + " " + last_name + ", you have not made the Dean's list or Honor Roll.")
        last_name = input("Please enter your last name or 'ZZZ' to quit: ")


