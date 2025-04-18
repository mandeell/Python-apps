def convert_to_snake_case(pascal_or_camel_cased_string):
    no_string_spaces = pascal_or_camel_cased_string.replace(' ', '')

    snake_cased_char_list = []

    for char in no_string_spaces:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

def main():
    print(convert_to_snake_case(input('Enter a short phrase: ')))

main()
