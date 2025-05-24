import re


class ExpressionParser:
    OPERATORS = {'+', '-', '*', '/', '%', '^', '(', ')'}
    PRECEDENCE = {'^': 4, '*': 3, '/': 3, '%': 3, '+': 2, '-': 2}

    @staticmethod
    def tokenize(expression):
        return re.findall(r"(\d+\.?\d*|[-+*/%^()]|MR|MS|MC|MA)", expression.upper())

    @staticmethod
    def to_postfix(tokens):
        output = []
        operators = []

        for token in tokens:
            if token.replace('.', '').isdigit():
                output.append(float(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            else:
                while (operators and operators[-1] != '(' and
                       ExpressionParser.PRECEDENCE.get(operators[-1], 0) >=
                       ExpressionParser.PRECEDENCE.get(token, 0)):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output