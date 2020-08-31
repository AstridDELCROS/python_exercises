import sys

def start():
    list = sys.argv
    len_list = len(list)
    if len_list != 3:
        exit("Bad number of arguments")
    if not list[1].isdigit or not list[2].isdigit():
        exit("Error, must be numbers")
    number1 = int(list[1])
    number2 = int(list[2])
    operation(number1, number2)

def operation(number1=8, number2=9):
    sum_list = (number1 + number2)
    print(sum_list)
    difference = (number1 - number2)
    print(difference)
    product = (number1 * number2)
    print(product)
    quotient = (number1 / number2)
    print(quotient)
    remainder = (number1 % number2)
    print(remainder)
start()
