def convert_to_snake_case(pascal_or_camel_cased_string):
    no_spaces_string = pascal_or_camel_cased_string.replace(' ', '')
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in no_spaces_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


def main():
    print(convert_to_snake_case(input('Enter a short phrase: ')))


main()