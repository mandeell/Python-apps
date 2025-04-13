def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2


# Basic Calculator
print('Welcome to this Basic Calculator')


while True:
    print('\nPlease choose an operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    operation = input(
        '\nEnter the number of the operation you want to perform: ')
    num1 = float(input('\nEnter first number: '))
    num2 = float(input('Enter second number: '))
    if operation == '1':
        print(addition(num1, num2))
    elif operation == '2':
        print(subtraction(num1, num2))
    elif operation == '3':
        print(multiplication(num1, num2))
    elif operation == '4':
        print(division(num1, num2))
    else:
        print('Invalid operation. Please try again.')

    again = input(
        'Do you want to perform another operation? (yes/no): ').lower().strip()
    if again != 'yes':
        print('\nThank you for using the calculator. Goodbye!')
        break
