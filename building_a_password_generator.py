import re
import secrets
import string


def generate_password():
    try:
        length = int(input('Input the length of the password: '))
        nums = int(input('Input the number of digits in the password: '))
        special_chars = int(input('Input the number of special characters in the password: '))
        uppercase = int(input('Input the number of uppercase characters in the password: '))
        lowercase = int(input('Input the number of lowercase characters in the password: '))
    except ValueError:
        raise ValueError("All inputs must be valid integers.")

    if any(val < 0 for val in [length, nums, special_chars, uppercase, lowercase]):
        raise ValueError("All input values must be non-negative integers.")

    if nums + special_chars + uppercase + lowercase > length:
        raise ValueError('Sum of digits, special characters, uppercase, and lowercase cannot exceed password length.')

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    while True:
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{re.escape(symbols)}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        if all(
            required <= len(re.findall(pattern, password))
            for required, pattern in constraints
        ):
            return password


if __name__ == '__main__':
    try:
        new_password = generate_password()
        print('Generated password:', new_password)
    except ValueError as ve:
        print(f"Input error: {ve}")
