from tkinter import *

def convert_miles_to_km():
    miles = float(user_input.get())
    kilometer = miles * 1.60934
    output_label.config(text = round(kilometer,2))

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady= 50)
window.resizable(width= False, height=False)

font_config  = ("Ariel", 14)

user_input = Entry(width=10, font=font_config)
user_input.focus()
# user_input.insert(END, string="0")
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles",font=font_config)
miles_label.grid(row= 0, column=2)

is_equal_label = Label(text="is equal to",font=font_config)
is_equal_label.grid(row= 1, column=0)

output_label = Label(text="0",font=font_config)
output_label.grid(row= 1, column=1)

km_label = Label(text="Km",font=font_config)
km_label.grid(row= 1, column=2)

calc_button = Button(font=font_config, text="Calculate", command=convert_miles_to_km)
calc_button.grid(row=2, column=1)






window.mainloop()