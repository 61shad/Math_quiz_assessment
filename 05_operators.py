# the user will choose what operation they want to do (addition, subtraction, multiplication, division)
def operator():
    while True:
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
            print("Sorry! That's not in the choices! Try again.")

while True:

        op_choice = input("""Please choose the operator of your quiz:
    1.➕
    2.➖
    3.❌
    4.➗
        """).lower()
