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
