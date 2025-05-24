import tkinter as tk

window = tk.Tk()
window.title("My First GUi Program")
window.minsize(width=800, height=500)

my_label = tk.Label(text="I Am a Label", font= ("Ariel", 24))
my_label.pack(side="left")




window.mainloop()
