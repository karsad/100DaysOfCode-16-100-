from tkinter import *

def button_clicked():
    my_label['text'] = input.get()
    input.delete(0, len(my_label['text']) )

my_window = Tk()
my_window.title("My First GUI program!")
my_window.minsize(width=500, height=500)
my_window.config(padx=50, pady=50)

my_label = Label(text="I am a label", font=("Courier", 28, "normal"))
my_label.grid(column=1, row=1)

input = Entry(width=20)
input.grid(column=4, row=3)

button = Button(text="Update text", command=button_clicked)
button_2 = Button(text="New Button")
button.grid(column=2, row=2)
button_2.grid(column=3, row=1)


my_window.mainloop()

