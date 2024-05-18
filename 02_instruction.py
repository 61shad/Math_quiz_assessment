
# User choose yes or no
def yes_no(question):

    while True:
        response = input(question).lower()

        # checking if user choose "y" or "n"
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


def instruction():
        print('''

    *** Instructions ***
    
    At first step you have to choose the level of difficulty you want to do, 
    level of difficulty are (Easy, Medium and Hard) 
    
    Next you should choose the number of questions you want to do, 
    for the infinite questions you can write <legend>.
    
    Good luck.
        ''')

# main routine goes here
print()
print("📝📝 Math  📝📝")
print()

want_instruction = yes_no("Do you want to read the instructions? ")

if want_instruction == "yes":
        instruction()

print("Program continues")
