
print("Calculator.")
first_num = 0
sec_num = 0
result = 0
operator = ''


def add_num(num1, num2):
    return num1 + num2


def subtract_num(num1, num2):
    return num1 - num2


def multiply_num(num1, num2):
    return num1 * num2


def divide_num(num1, num2):
    return num1 / num2


valid_first_num = False
while not valid_first_num:
    try:
        first_num = int(input("Please enter the first number"))
    except ValueError:
        print("That is not a valid number")
        continue

    if isinstance(first_num, int) or isinstance(first_num, float):
        valid_first_num = True
    else:
        print("That is not a valid number")
        continue

valid_sec_num = False
while not valid_sec_num:
    sec_num = int(input("Please enter the second number"))
    if isinstance(sec_num, int) or isinstance(sec_num, float):
        valid_sec_num = True
    else:
        print("That is not a valid number")
        continue

valid_operator = False
while not valid_operator:
    operator = input("Please enter the operator for those two numbers "
                     "(* is multiply, / is divide, - is subtract, + is add)")
    print(operator)
    if operator == '*':
        valid_operator = True
        result = multiply_num(first_num, sec_num)
    elif operator == '/':
        if sec_num == 0:
            print("Cannot divide by zero!")
            continue
        else:
            valid_operator = True
            result = divide_num(first_num, sec_num)
    elif operator == '-':
        valid_operator = True
        result = subtract_num(first_num, sec_num)
    elif operator == '+':
        valid_operator = True
        result = add_num(first_num, sec_num)
    else:
        print("That is not a valid number")
        continue

print("the result of %d %s %d is %d" % (first_num, operator, sec_num, result))
