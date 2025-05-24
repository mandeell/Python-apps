from operations import MathOperations
from memory import MemoryManager
from history import CalculationHistory
from parser import ExpressionParser


class ScientificCalculator:
    def __init__(self):
        self.operations = MathOperations()
        self.memory = MemoryManager()
        self.history = CalculationHistory()
        self.parser = ExpressionParser()

        self.operation_map = {
            '+': self.operations.add,
            '-': self.operations.subtract,
            '*': self.operations.multiply,
            '/': self.operations.divide,
            '%': self.operations.modulo,
            '^': self.operations.power
        }

    def calculate(self, expression):
        try:
            # Handle memory commands
            if expression.upper() == 'MR':
                return self.memory.recall()

            # Parse and evaluate
            tokens = self.parser.tokenize(expression)
            postfix = self.parser.to_postfix(tokens)
            result = self._evaluate(postfix)

            # Store in history
            self.history.add_entry(expression, result)
            return result

        except Exception as e:
            return f"Error: {str(e)}"

    def _evaluate(self, postfix):
        stack = []
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                operation = self.operation_map[token]
                result = operation(a, b)
                print(f"Step: {a} {token} {b} = {result}")
                stack.append(result)
        return stack[0] if stack else 0

    def show_history(self):
        """Display calculation history"""
        return self.history.get_history()

    def clear_history(self):
        """Clear calculation history"""
        return self.history.clear_history()