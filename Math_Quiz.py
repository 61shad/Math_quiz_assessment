import random

# User choose yes or no, if they wanted to read instruction they will choose yes and if they didn't wanted choose no.
def yes_no(question):

    while True:
        response = input(question).lower()
        # checking if user choose "y" or "n"
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


# the instruction for the quiz. It shows the user what to do.
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


# check how many question the user choose, or they want to do infinite question.
def how_many_question(question):
    print(question)

    while True:
        # if the user didn't enter a number the error will pop up and tell them to enter number.
        error = "Please enter your answer as a number. or press <enter> for infinite questions."

        to_check = input().lower()
        # checks if the user picked infinite mode
        if to_check == "":
            return -1
        try:
            response = int(to_check)
            # check that answer is more than 0
            if response <= 0:
                print(error)
            else:
                return response
        # if something wrong the error will show
        except ValueError:
            print(error)


# the user will choose what operation they want to do (addition, subtraction, multiplication, division)
def operator():
    while True:

        op_choice = input("""Please choose the operator of your quiz:
1.➕
2.➖
3.❌
4.➗
    """).lower()
        # Checking the user's choice
        if op_choice in ['1', '+']:
            return "+"
        elif op_choice in ['2', '-']:
            return "-"
        elif op_choice in ['3', '*']:
            return "*"
        elif op_choice in ['4', '/']:
            return "/"
        else:
            print("Sorry! That's not in the choices! Try again. ")


# Function to generate a math question based on the chosen level and operation
def level_choosing():
    print("""Choose the level of difficulty you want to do:"
🟢 1.beginner 
🟡 2.intermediate
🟠 3.advanced
🔴 4.expert
    """)
    # Depending on the level, generate random numbers within specific ranges
    while True:
        level = input()
        if level == "beginner" or level == "1":
            print("You choose the easy level! Good Luck! 😀")
            return 1,10

        elif level == "intermediate" or level == "2":
            print("You choose the intermediate level! Good Luck! 😁")
            return -10, 100

        elif level == "advanced" or level == "3":
            print("You choose the advanced level! Good Luck! 😎")
            return -100, 1000

        elif level == "expert" or level == "4":
            print("You choose the expert level! Good Luck! 😮")
            return -1000, 10000
        else:
            # Return an error message for invalid level choices
            print("I am not sure if it's a level. 🤔")

# Calculate the correct answer based on the chosen operation
def calculate_answer(num1,num2,operator):

    # the equation based on the operation
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        # make sure the division is valid and they don't divide it by zero
        if num2 == 0:
            num2 = 1
        # round the decimal numbers to the nearest full number
        answer = round(num1 / num2)
    # this will return the right answer if the answer was wrong
    return answer

# variables for history
question_content =[]
user_answer_history=[]
correct_answer_history=[]

# main routine goes here

#
total_correct_questions = 0
total_wrong_questions = 0

print()
print("📝📝 Math  📝📝")
print()

# ask the user if they want to read instructions
want_instruction = yes_no("Do you want to read the instructions? ")
# exit signal is a variable to mark that if player wanna exit
exit_signal=True
# the question that the user is answering
current_question=1

# check if they choose "yes" or "no"
if want_instruction == "yes":
    instruction()

# Check what operator the user want to do
#(addition, subtraction, multiplication, and division)
chosen_operator = operator()
print("You chose", chosen_operator, "for your quiz.")

# ask the user how many question they want to be asked
question_left = how_many_question("How many questions do you want to answer? For infinite questions, please press <enter>.")
level = level_choosing()
# level[0] : min of the boundary
# level[1] : max of the random boundary
#boudary of ( beginner, intermediate, advanced, expert) levels
while question_left!=0 and exit_signal:
    num1=random.randint(level[0],level[1])
    num2=random.randint(level[0],level[1])

    # print the equation for the player to answer
    print(f"What is {num1} {chosen_operator} {num2}?")
    # store the questions and the answer for the history, if the user wanted to see at the end of the quiz
    correct_answer = calculate_answer(num1, num2, chosen_operator)
    question_content.append(f"What is {num1} {chosen_operator} {num2}?")
    correct_answer_history.append(correct_answer)
    # checks if the user enters the correct answer or the wrong answer (answer checker)
    while True:

        user_answer = input("Your answer: ").lower()
        try:

            # exit code
            if user_answer == "i am done":
                exit_signal = False
                print("Okay! Bye Bye 🤚")
                current_question = current_question - 1
                break

            user_answer = int(user_answer)
            # if the answer is correct
            if user_answer == correct_answer:
                print("Good job! You got it right! 😯")
                total_correct_questions = total_correct_questions + 1
                user_answer_history.append(user_answer)
                break

            # if the answer is wrong
            else:
                print(f"Sorry, the correct answer is {correct_answer} 😐")
                user_answer_history.append(user_answer)
                break

        except ValueError:
            # if the user entered an answer which is not number (the error)
            print("❗ Can you please enter a number: ")

    # every question user do, question_left will decrease by 1, and current_question will increase by 1
    question_left = question_left-1
    current_question = current_question + 1

# if the user didn't answer any question and wanted to exit the quiz
if current_question == 1:
    print("You did not answer any question. 🤔")

else:
    # ask the question if the user want to see the history or not
    if yes_no("Do you want to see the history? "):
        # if user wanted to see history will be displayed
        print("⌛ History ⌛")
        for i in range(2, current_question + 1):
            # shows the question number
            print(f"Question {i - 1}: ")
            # it shows the question and the correct answer
            print(f"Question: {question_content [i - 2]}  (Correct answer: {correct_answer_history [i - 2]})")
            # it shows the user answer
            print(f"sYour answer: {user_answer_history [i - 2]}")

# statistics to show
print("📒 statistics 📒")
print(f"✍ You answered {current_question-1} questions.")
print(f"✔ You answered {total_correct_questions} questions right.")
print(f"🔢 You answered {(total_correct_questions * 100) / (current_question - 1)}% of the questions correct")
print(f"❌ You answered {current_question-1-total_correct_questions} wrong.")