def arithmetic_arranger(problems, show_answers=False):

# Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

# Initialize lists to store formatted lines
    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts

    # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate numbers (only digits)
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Validate number length (max 4 digits)
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Convert numbers to integers
        num1_int = int(num1)
        num2_int = int(num2)

        # Calculate answer if needed
        if operator == '+':
            answer = num1_int + num2_int
        else:
            answer = num1_int - num2_int

        # Determine width (length of longest operand or answer plus operator space)
        max_width = max(len(num1), len(num2)) + 2  # +2 for operator and space

        # Format lines
        top_line.append(num1.rjust(max_width))
        bottom_line.append(operator + ' ' + num2.rjust(max_width - 2))
        dash_line.append('-' * max_width)
        if show_answers:
            answer_line.append(str(answer).rjust(max_width))

    # Join lines with four spaces between problems
    formatted = []
    formatted.append('    '.join(top_line))
    formatted.append('    '.join(bottom_line))
    formatted.append('    '.join(dash_line))
    if show_answers:
        formatted.append('    '.join(answer_line))

    # Return as a single string with newlines
    return '\n'.join(formatted)


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')