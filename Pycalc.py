#calculator.py


first_number = input("input number:")

print("Your first number is: " + str(first_number))

operator = input("""choose an operation. /n
                    For addition type 'add' /n
                    For subtraction type 'subtr'""")


second_number = input("input second number")

print("your second number is:" + str(second_number))

if operator == 'add':
    print(int(first_number) + int(second_number))

if operator == 'subtr':
    print(int(first_number) + int(second_number))


