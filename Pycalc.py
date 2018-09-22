#calculator.py

#create a list of valid operators
operators = ['+','-']

#Asks user for an input number
input_number = input("input number:")

#checks whether entry is numeric
while isnumeric(input_number) == False:

    #When entry is not a number, prints error message
    print("not a number")

    #When entry is not a number, asks user for an input number
    input_number = input("input number:")

    #Loop breaks when input is numeric

input_operator = input("input operator:")

while input_operator not in operators:

    print("choose a different operator")

    input_operator = input("input operator")

input_second_number = input("input second number")

while isnumeric(input_second_number) == False:

    print("not a number")

    input_second_number = input("input second number")

evaluate = input("evaluate? Y/N")

if evaluate == "y" or "Y":

    print(input_number)
    print(input_operator)
    print(input_second_number)



