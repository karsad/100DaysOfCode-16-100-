from tkinter import messagebox
from tkinter import *
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_tb.delete(0, END)
    password_tb.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_tb.get()
    login = login_tb.get()
    password = password_tb.get()

    if website == "" or login == "" or password == "":
        messagebox.showinfo(message="Fields can not be empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"Adding {website}", message=f"Are you sure you want to add new credentials for "
                                                                  f"{website}?\n{login}/{password}")
        if is_ok:
            with open ("data.txt", "a") as file:
                file.write(f"{website} | {login} | {password}\n")

                website_tb.delete(0, END)
                password_tb.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

my_window = Tk()
my_window.title("Passwd Manager")
my_window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

label1 = Label(text="Website:", font=("",16), justify="right", width=15)
label1.grid(row=2, column=1)

label2 = Label(text="Email/Username:", font=("",16), justify="right", width=15)
label2.grid(row=3, column=1)

label3 = Label(text="Password:", font=("",16), justify="right", width=15)
label3.grid(row=4, column=1)

website_tb = Entry(width=43)
website_tb.grid(row=2, column=2, columnspan=2)
website_tb.focus()

login_tb = Entry(width=43)
login_tb.grid(row=3, column=2, columnspan=2)
login_tb.insert(END, "my_email@gmail.com")

password_tb = Entry(width=25)
password_tb.grid(row=4, column=2)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=4, column=3)

add_btn = Button(text="Add",width=40, command=save_password)
add_btn.grid(row=5, column=2, columnspan=2)

my_window.mainloop()