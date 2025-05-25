from tkinter import *

def button_clicked():
    my_label.config(text = input.get())


window = Tk()
window.title("My First GUi Program")
window.minsize(width=1500, height=800)
window.config(padx=40, pady=40)
window.configure(bg="beige")
# Label
label_font_config = ("Ariel", 24)
button_font_config = ("Ariel", 14)
entry_font_config = ("Ariel", 14)


my_label = Label(text="I Am a Label", font= label_font_config, bd= 5)
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

# button
button = Button(font= button_font_config, text="Click Me!", bd=5, command=button_clicked)
button.grid(column=1, row=1,padx=30, pady=20)

button1 = Button(font= button_font_config, text="Click Me!", bd=5, command=button_clicked)
button1.grid(column=2, row=0, padx=40)

# Entry
input = Entry(font=entry_font_config, bd = 5, width=30)
print(input.get())
input.grid(column=3, row=3, padx=40, pady=30)




window.mainloop()
