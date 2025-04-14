import tkinter as tk

def is_button_clicked():
    value = input_km.get()
    input_km.delete(0, len(value))
    miles = float(value)*0.621371
    result.config(text=f"{miles:.2f}")

my_window = tk.Tk()
my_window.minsize(width=300, height=300)
my_window.config(padx=30, pady=30)
my_window.title("km to miles converter v1.0")

input_km = tk.Entry()
input_km.config(width=5, justify="center")
input_km.grid(column=2, row=1)

label1 = tk.Label()
label1.config(text="km", justify="left")
label1.grid(row=1, column=3)

label2 = tk.Label()
label2.config(text="is equal to:", justify="right")
label2.grid(row=2, column=1)

result = tk.Label()
result.config(text="-", justify="center")
result.grid(row=2, column=2)

label3 = tk.Label()
label3.config(text="miles", justify="left")
label3.grid(row=2, column=3)

button = tk.Button()
button.config(text="Convert!", command=is_button_clicked)
button.grid(row=3, column=2)

my_window.mainloop()