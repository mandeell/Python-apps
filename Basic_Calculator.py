import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, scrolledtext

class Calculator:
    def __init__(self):
        self.operations = {
            '1': ('addition', self.addition),
            '2': ('subtraction', self.subtraction),
            '3': ('multiplication', self.multiplication),
            '4': ('division', self.division)
        }

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

    def get_operation_name(self, op):
        return self.operations.get(op, ('invalid', None))[0]

    def get_operation_func(self, op):
        return self.operations.get(op, ('invalid', None))[1]

class DatabaseManager:
    def __init__(self, db_name='calculations.db'):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()
        self._create_table()

    def _create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT,
                num1 REAL,
                num2 REAL,
                result TEXT
            )
        ''')
        self._conn.commit()

    def save_calculation(self, operation, num1, num2, result):
        self._cursor.execute('''
            INSERT INTO calculations (operation, num1, num2, result)
            VALUES (?, ?, ?, ?)
        ''', (operation, num1, num2, str(result)))
        self._conn.commit()

    def get_history(self):
        self._cursor.execute('SELECT operation, num1, num2, result FROM calculations')
        return self._cursor.fetchall()

    def clear_history(self):
        self._cursor.execute('DELETE FROM calculations')
        self._conn.commit()

    def close(self):
        self._conn.close()

class CalculatorGUI:
    def __init__(self, calculator, db_manager):
        self.calculator = calculator
        self.db_manager = db_manager
        self.root = tk.Tk()
        self.root.title("Basic Calculator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self._setup_gui()

    def _setup_gui(self):
        # Operation selection
        tk.Label(self.root, text="Select Operation:").pack(pady=5)
        self.operation_var = tk.StringVar()
        operation_menu = ttk.Combobox(self.root, textvariable=self.operation_var, values=[
            "1. Addition", "2. Subtraction", "3. Multiplication", "4. Division"
        ], state="readonly")
        operation_menu.pack(pady=5)
        operation_menu.set("1. Addition")

        # Number inputs
        tk.Label(self.root, text="Enter First Number:").pack(pady=5)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack(pady=5)

        tk.Label(self.root, text="Enter Second Number:").pack(pady=5)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack(pady=5)

        # Result display
        self.result_label = tk.Label(self.root, text="Result: ", wraplength=350)
        self.result_label.pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Calculate", command=self._calculate).pack(pady=5)
        tk.Button(self.root, text="View History", command=self._view_history).pack(pady=5)
        tk.Button(self.root, text="Clear History", command=self._clear_history).pack(pady=5)

    def _calculate(self):
        op = self.operation_var.get()[0]  # Get operation number (e.g., '1')
        selected_op = self.calculator.get_operation_name(op)
        if selected_op == 'invalid':
            self.result_label.config(text="Result: Invalid operation")
            return

        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            self.result_label.config(text="Result: Invalid number input")
            return

        operation_func = self.calculator.get_operation_func(op)
        result = operation_func(num1, num2)
        self.result_label.config(text=f"Result: {result}")
        self.db_manager.save_calculation(selected_op, num1, num2, result)

    def _view_history(self):
        history_window = Toplevel(self.root)
        history_window.title("Calculation History")

        # Calculate dynamic height based on number of history entries
        history = self.db_manager.get_history()
        num_entries = len(history)
        # Base height + 20 pixels per entry, capped at 600 pixels
        dynamic_height = min(150 + num_entries * 20, 600)
        history_window.geometry(f"500x{dynamic_height}")

        history_text = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, width=60, height=20)
        history_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        if not history:
            history_text.insert(tk.END, "No calculations in history.")
        else:
            for calc in history:
                operation, num1, num2, result = calc
                history_text.insert(tk.END, f"{operation}: {num1} {operation[0]} {num2} = {result}\n")
        history_text.config(state='disabled')

    def _clear_history(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the calculation history?"):
            self.db_manager.clear_history()
            messagebox.showinfo("Success", "Calculation history cleared.")

    def run(self):
        self.root.mainloop()
        self.db_manager.close()

if __name__ == "__main__":
    calculator1 = Calculator()
    db_manager1 = DatabaseManager()
    gui = CalculatorGUI(calculator1, db_manager1)
    gui.run()