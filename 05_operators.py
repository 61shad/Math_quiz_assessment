def operator():
    choice = input("""Please choose the operator of your quiz:
    1. +
    2. -
    3. x
    4. /
    """)
    while True:
        if choice == "1" or choice == "+":
            return "+"
        elif choice == "2" or choice == "-":
            return "-"
        elif choice == "3" or choice == "x":
            return "x"
        elif choice == "4" or choice == "/":
            return "/"
        else:
            print("Sorry! That's not in the choices! Try again. ")

a=operator()
print(a)