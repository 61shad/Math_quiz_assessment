# check that user enter an integer
def int_checker():


    while True:
        error = "Please enter your answer as a number."

        try:
            response = int(input("Enter your answer: "))

            # check that answer is more than 0
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
target_score = int_checker()
print(target_score)