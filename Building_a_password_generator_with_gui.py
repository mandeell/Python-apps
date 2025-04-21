import tkinter as tk
from tkinter import messagebox
import re
import secrets
import string


# ---------- Password Strength Checker ----------
def check_strength(pwd):
    score = 0
    if len(pwd) >= 8:
        score += 1
    if re.search(r"[A-Z]", pwd):
        score += 1
    if re.search(r"[a-z]", pwd):
        score += 1
    if re.search(r"[0-9]", pwd):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"


# ---------- Password Generator Logic ----------
def generate_password_gui():
    try:
        length = int(length_entry.get())
        nums = int(digits_entry.get())
        special_chars = int(specials_entry.get())
        uppercase = int(upper_entry.get())
        lowercase = int(lower_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "All input fields must be integers.")
        return

    if any(val < 0 for val in [length, nums, special_chars, uppercase, lowercase]):
        messagebox.showerror("Input Error", "All input values must be non-negative.")
        return

    if nums + special_chars + uppercase + lowercase > length:
        messagebox.showerror("Input Error", "Sum of constraints cannot exceed password length.")
        return

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + symbols

    max_attempts = 1000
    attempts = 0

    while attempts < max_attempts:
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{re.escape(symbols)}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        if all(required <= len(re.findall(pattern, password)) for required, pattern in constraints):
            password_output.delete(0, tk.END)
            password_output.insert(0, password)

            # 🔄 Adjust width to fit the password
            min_width = 15
            calculated_width = max(min_width, len(password))
            password_output.config(width=calculated_width)

            # Show strength
            strength, color = check_strength(password)
            strength_label.config(text=f"Strength: {strength}", fg=color)
            return

        attempts += 1

    messagebox.showerror("Generation Error", "Could not generate password with the given constraints.")


def copy_to_clipboard():
    pwd = password_output.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


def toggle_dark_mode():
    global is_dark
    is_dark = not is_dark
    update_theme()


def update_theme():
    theme = dark_theme if is_dark else light_theme
    root.configure(bg=theme['bg'])

    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button) or isinstance(widget, tk.Entry):
            widget.configure(bg=theme['bg'], fg=theme['fg'])
        if isinstance(widget, tk.Entry):
            widget.configure(insertbackground=theme['fg'])

    strength_label.configure(bg=theme['bg'])


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("1200x650")
root.resizable(False, False)

font_config = ("Arial", 12)

light_theme = {'bg': '#ffffff', 'fg': '#000000'}
dark_theme = {'bg': '#1e1e1e', 'fg': '#ffffff'}
is_dark = False

# Fields
fields = [
    ("Password Length:", "length_entry"),
    ("Number of Digits:", "digits_entry"),
    ("Number of Special Characters:", "specials_entry"),
    ("Number of Uppercase Letters:", "upper_entry"),
    ("Number of Lowercase Letters:", "lower_entry")
]

entries = {}

for idx, (label_text, var_name) in enumerate(fields):
    label = tk.Label(root, text=label_text, font=font_config)
    label.grid(row=idx, column=0, padx=20, pady=10, sticky="e")

    entry = tk.Entry(root, font=font_config, width=10)
    entry.grid(row=idx, column=1, padx=20, pady=10, sticky="w")
    entries[var_name] = entry

length_entry = entries["length_entry"]
digits_entry = entries["digits_entry"]
specials_entry = entries["specials_entry"]
upper_entry = entries["upper_entry"]
lower_entry = entries["lower_entry"]

# Buttons
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"),
                            bg="#4CAF50", fg="white", command=generate_password_gui)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 12),
                        bg="#2196F3", fg="white", command=copy_to_clipboard)


# Password Output + Copy Button
output_frame = tk.Frame(root, bg=root['bg'])
output_frame.grid(row=8, column=0, columnspan=2, pady=10)

current_theme = dark_theme if is_dark else light_theme
tk.Label(output_frame, text="Generated Password:", font=font_config, bg=current_theme['bg'], fg=current_theme['fg']).grid(row=0, column=0, padx=10, sticky="e")


password_output = tk.Entry(output_frame, font=("Courier", 14))
password_output.grid(row=0, column=1, padx=10)

copy_button = tk.Button(output_frame, text="📋", font=("Arial", 12), bg="#2196F3", fg="white", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=5)

# Strength Indicator
strength_label = tk.Label(root, text="Strength: ", font=font_config)
strength_label.grid(row=9, column=0, columnspan=2, pady=5)

# Dark Mode Toggle (top-right corner)
dark_mode_btn = tk.Button(root, text="🌓 Toggle Dark Mode", font=("Arial", 10),
                          bg="#444", fg="white", command=toggle_dark_mode)
dark_mode_btn.place(relx=1.0, x=-10, y=10, anchor="ne")

# Apply theme
update_theme()

# Run GUI
root.mainloop()
