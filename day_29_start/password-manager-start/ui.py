from tkinter import *

WHITE = "white"

def setup_ui(window, generate_password, save, copy_to_clipboard, find_password):
    """Set up the Password Manager UI and return entry widgets."""
    window.title("Password Manager")
    window.config(padx=100, pady=100, bg=WHITE)
    window.resizable(width=False, height=False)

    # Canvas with logo
    canvas = Canvas(width=400, height=400, highlightthickness=0, bg=WHITE)
    logo_img = PhotoImage(file="logo_resized_2x.png")
    canvas.create_image(200, 200, image=logo_img)
    canvas.grid(row=0, column=1)
    canvas.image = logo_img  # Keep reference to avoid garbage collection

    # Website
    website_label = Label(text="Website:", bg=WHITE)
    website_label.grid(row=1, column=0)

    website_entry = Entry( highlightthickness=0, bg=WHITE)
    website_entry.focus()
    website_entry.grid(row=1, column=1, pady=10,sticky="EW")

    # Email/Username
    email_username_label = Label(text="Email/Username:", bg=WHITE)
    email_username_label.grid(row=2, column=0)

    email_username_entry = Entry( bg=WHITE, highlightthickness=0)
    email_username_entry.insert(0, "nelsonokiki@gmail.com")
    email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

    # Password
    password_label = Label(text="Password:", bg=WHITE)
    password_label.grid(row=3, column=0)

    password_entry = Entry( bg=WHITE, highlightthickness=0)
    password_entry.grid(row=3, column=1, pady=10, sticky="EW")

    # Buttons
    generate_button = Button(
        text="Generate Password",
        bg=WHITE,
        highlightthickness=0,
        command=generate_password,
        activebackground="#D34A3F",
        activeforeground=WHITE
    )
    generate_button.grid(row=3, column=2, sticky="EW")

    add_button = Button(
        text="Add",
        highlightthickness=0,
        bg=WHITE,
        width=35,
        command=save,
        activebackground="#D34A3F",
        activeforeground=WHITE
    )
    add_button.grid(row=4, column=1, columnspan=2, pady=10, sticky="EW")

    search_button = Button(
        text="Search",
        bg=WHITE,
        activebackground="#D34A3F",
        activeforeground=WHITE,
        command=find_password
    )
    search_button.grid(row=1, column=2, padx=5,sticky="EW")

    copy_button = Button(
        text="📋",
        font=("Arial", 12),
        bg="#D34A3F",
        fg="white",
        command=copy_to_clipboard
    )
    copy_button.grid(row=3, column=3, padx=5)

    return website_entry, email_username_entry, password_entry, search_button