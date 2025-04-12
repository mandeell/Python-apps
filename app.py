# import time
# from tokenize import String


# def countdown_timer(seconds):
#     while seconds:
#         mins, secs = divmod(seconds, 60)
#         timer = f'{mins:02}:{secs:02}'
#         print(timer, end='\r')
#         time.sleep(1)
#         seconds -= 1

#     print("Time's up!")


# if __name__ == "__main__":
#     try:
#         total_seconds = int(input("Enter the countdown time in seconds: "))
#         countdown_timer(total_seconds)
#     except ValueError:
#         print("Please enter a valid number.")

# num1 = float(input('Enter first number: '))
# num2 = float(input('Enter second number: '))

def addition(num1, num2):
    return (num1 + num2)


def subtraction(num1, num2):
    return (num1 - num2)


def multiplication(num1, num2):
    return (num1 * num2)


def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return (num1 / num2)


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
