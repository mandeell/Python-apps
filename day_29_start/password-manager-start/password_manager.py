from tkinter import *
from tkinter import messagebox
import secrets, string, random, re, json
from ui import setup_ui

WHITE="white"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    length = random.randint(12,20)
    nums = random.randint(1,3)
    special_chars = random.randint(1,3)
    uppercase = random.randint(1,3)
    lowercase = random.randint(1,3)

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
            if len(website_entry.get()) != 0:
                password_entry.delete(0, END)
                password_entry.insert(0, password)
                break
            else:
                messagebox.showerror(title="Error", message="Enter the name of the website")
                break
            # return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    email_username = email_username_entry.get()
    website = website_entry.get()
    new_data = {
        website.title(): {
            "email": email_username,
            "password": password
        }
    }

    if  len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- COPY TO CLIPBOARD ------------------------------- #
def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        window.clipboard_clear()
        window.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if not website.title():
        messagebox.showwarning(
            title="Empty Field",
            message="Please enter a website to search!"
        )
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        if website.title() in data:
            email = data[website.title()]["email"]
            password = data[website.title()]["password"]
            messagebox.showinfo(
                title=website.title(),
                message=f"Email: {email}\nPassword: {password}"
            )
            search_button.config(
                bg="#D34A3F",
                fg=WHITE
            )
        else:
            messagebox.showinfo(
                title="Not Found",
                message=f"No details for {website} found."
            )
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found. Save some passwords first!")


if __name__ == "__main__":
    window = Tk()
    website_entry, email_username_entry, password_entry, search_button = setup_ui(window, generate_password, save, copy_to_clipboard, find_password)
    window.mainloop()