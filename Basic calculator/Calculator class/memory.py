class MemoryManager:
    def __init__(self):
        self._memory = 0

    @property
    def memory(self):
        return self._memory

    def store(self, value):
        self._memory = value
        return f"Stored {value} in memory"

    def recall(self):
        return self._memory

    def clear(self):
        self._memory = 0
        return "Memory cleared"

    def add(self, value):
        self._memory += value
        return f"Added {value} to memory"