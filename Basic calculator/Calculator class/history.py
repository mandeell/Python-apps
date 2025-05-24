class CalculationHistory:
    def __init__(self):
        self._history = []

    def add_entry(self, expression, result):
        self._history.append(f"{expression} = {result}")

    def get_history(self):
        return "\n".join(self._history)

    def clear_history(self):
        self._history = []
        return "History cleared"

    @property
    def entries(self):
        """Get raw history entries"""
        return self._history.copy()