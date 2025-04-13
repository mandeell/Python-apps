def addition(anum1, anum2):
    return anum1 + anum2


def subtraction(bnum1, bnum2):
    return bnum1 - bnum2


def multiplication(cnum1, cnum2):
    return cnum1 * cnum2


def division(fnum1, fnum2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return fnum1 / fnum2


def operation(ope):
    operations = {
        '1': 'addition',
        '2': 'subtraction',
        '3': 'multiplication',
        '4': 'division'
    }
    return operations.get(ope, 'invalid')

# Basic Calculator
print('Welcome to this Basic Calculator')


while True:
    print('\nPlease choose an operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')


    op = input(
        '\nEnter the number of the operation you want to perform: ')

    selected_op = operation(op)
    print(f'\nYou have selected an {selected_op} operation')

    if selected_op == 'invalid':
        print('Please try again.')
        continue


    num1 = float(input('\nEnter first number: '))
    num2 = float(input('Enter second number: '))
    if op == '1':
        print(addition(num1, num2))
    elif op == '2':
        print(subtraction(num1, num2))
    elif op == '3':
        print(multiplication(num1, num2))
    elif op == '4':
        print(division(num1, num2))
    else:
        print('Invalid operation. Please try again.')

    again = input(
        'Do you want to perform another operation? (yes/no): ').lower().strip()
    if again != 'yes':
        print('\nThank you for using the calculator. Goodbye!')
        break
