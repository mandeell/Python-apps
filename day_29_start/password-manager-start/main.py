from tkinter import *
from tkinter import messagebox
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_entry.get()
    email_username = email_username_entry.get()
    website = website_entry.get()

    if not website or not email_username or not password:
        messagebox.showwarning("Empty Field", "Please don't leave any field empty!")
        return

    file_exists = os.path.exists("data.txt")
    with open("data.txt", "a") as file:
        if not file_exists:
            file.write("Website | Email/Username | Password\n")
        file.write(f"{website} | {email_username} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config( padx=100, pady=100)


canvas = Canvas(width=400, height=400,highlightthickness=0)
logo_img = PhotoImage(file="logo_resized_2x.png")
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, pady=10)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=45)
email_username_entry.insert(0, string="nelsonokiki@gmail.com")
email_username_entry.grid(row=2, column=1,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1,pady=10)

generate_button = Button(text="Generate Password", highlightthickness=0)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)







window.mainloop()