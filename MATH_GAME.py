import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of item in the list
            elif user_response == item[0]:
                return item


        # print error if the user doesn't enter a vaild response
        print(error)
        print()


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

    At first step you should choose what operator you want to work with
    (addition, subtraction, multiplication and division).
     
    Next have to choose the level of difficulty you want to do, 
    level of difficulty are (Easy, Medium and Hard) 

    After that, you should choose the number of questions you want to do, 
    for the infinite questions you can write <inf>.
    
    If you wanted to exit the code, just write <done>. 
    
    At the end you can see your quiz history. If you wanted to see the history
    write yes and then you can check the history.
    
    Get Ready!!
    see you in the quiz!

    Good luck.
        ''')


# check that user enter an integer
def int_check(question):


    while True:
        error = "Please enter your answer as a number."

        to_check = input(question)

        # check the infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that answer is more than 0
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def operator():
    while True:
        op_choice = input("""Please choose the operator of your quiz:
    1.➕
    2.➖
    3.❌
    4.➗
        """)

        # Checking the user's choice
        if op_choice in ['1', '+']:
            return "+"
        elif op_choice in ['2', '-']:
            return "-"
        elif op_choice in ['3', 'x']:
            return "x"
        elif op_choice in ['4', '/']:
            return "/"
        else:
            print("Sorry! That's not in the choices! Try again.")



# main routine goes here
print()
print("📝📝 Math  📝📝")
print()

# ask the user if they want to read instructions
want_instruction = yes_no("Do you want to read the instructions? ")

# check if they choose "yes" or "no"
if want_instruction == "yes":
    instruction()

# Check what operator the user want to do
#(addition, subtraction, multiplication, and division)
chosen_operator = operator()
print("You chose", chosen_operator, "for your quiz.")

# ask the user how many question they want to be asked
num_questions = int_check("How many questions do you want to answer? for infinite questions press <enter>.")

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 5

print("Program continues")
