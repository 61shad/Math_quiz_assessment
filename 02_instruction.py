
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

    Next you should choose the number of questions you want to do, 
    for the infinite questions you can write <inf>.

    After that, you have to choose the level of difficulty you want to do, 
    level of difficulty are (Easy, Medium, Hard and expert). When you choose the
    level of the questions then the questions woould be asked. 

    If you wanted to exit the code, just write <i am done>. Keep in mind that 
    you can only exit when you are answering the questions and you cannot exit
    the quiz in other stages. Also please use lower case not apper case.

    At the end you can see your quiz history. If you wanted to see the history
    write yes and then you can check the history. But if you did not wanted to see
    the history then type no. It will skip the history and shows you the statistics. 

    Get Ready!!
    See you in the quiz!
    Good luck!
        ''')

# main routine goes here
print()
print("📝📝 Math  📝📝")
print()

want_instruction = yes_no("Do you want to read the instructions? ")

if want_instruction == "yes":
        instruction()

print("Program continues")
