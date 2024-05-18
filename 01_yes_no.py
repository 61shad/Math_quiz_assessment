# User choose yes or no
def yes_no(question):

    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

# main routine goes here
while True:
    want_instruction = yes_no("Do you want to read the instructions? ")
    print(f"you choose {want_instruction}")