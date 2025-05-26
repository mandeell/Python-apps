from tkinter import *
from tkinter import messagebox
import secrets, string, random, re, os

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
            password_entry.delete(0, END)
            password_entry.insert(0, password)
            break
            # return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    email_username = email_username_entry.get()
    website = website_entry.get()

    if  len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: "f"\nEmail: "
                                                      f"{email_username}\nPassword: {password}"
                                                      f"\nIs it okay to save?")
        if is_okay:
            file_exists = os.path.exists("data.txt")
            with open("data.txt", "a") as file:
                if not file_exists:
                    file.write("Website | Email/Username | Password\n")
                file.write(f"{website} | {email_username} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        window.clipboard_clear()
        window.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config( padx=100, pady=100)
window.resizable(width=False, height=False)


canvas = Canvas(width=400, height=400,highlightthickness=0)
logo_img = PhotoImage(file="logo_resized_2x.png")
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=45,bg="#d9d9d9", highlightthickness=0)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=10)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=45, bg="#d9d9d9", highlightthickness=0)
email_username_entry.insert(0, string="nelsonokiki@gmail.com")
email_username_entry.grid(row=2, column=1,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=27, bg="#d9d9d9", highlightthickness=0)
password_entry.grid(row=3, column=1,pady=10)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)







window.mainloop()