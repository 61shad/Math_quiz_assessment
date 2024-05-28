# Function to generate a math question based on the chosen level and operation
def level_choosing():
    print("""Choose the level of difficulty you want to do:"
            1.beginner 
            2.intermediate
            3.advanced
            4.expert
    """)

    # Depending on the level, generate random numbers within specific ranges
    while True:
        level = input()
        if level == "beginner" or level == "1":
            print("You choose the beginner level! Good Luck! 😀")
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


print(level_choosing())