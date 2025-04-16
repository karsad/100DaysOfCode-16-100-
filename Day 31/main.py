from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORDS_DATA = []
CARD_TIMER = None
CURRENT_WORD = None

def update_database():
    global CURRENT_WORD
    WORDS_DATA.remove(CURRENT_WORD)
    save_data_to_file(WORDS_DATA)
    get_random_word()


# -------------------------------------- READ FILE -------------------------------------- #
def get_data_from_file():
    global WORDS_DATA
    try:
        with open("data/french_words_to_learn.csv", "r") as data_file:
            my_data = pandas.read_csv(data_file)
    except FileNotFoundError:
        with open("data/french_words.csv", "r") as data_file:
            my_data = pandas.read_csv(data_file)
    finally:
        WORDS_DATA = my_data.to_dict(orient="records")

def save_data_to_file(data_dict):
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/french_words_to_learn.csv", index=False)

# ----------------------------------- CARD OPERATIONS ----------------------------------- #

def get_random_word():
    global WORDS_DATA, CARD_TIMER, CURRENT_WORD
    if CARD_TIMER != None: my_screen.after_cancel(CARD_TIMER)
    canvas.itemconfig(my_card, image=card_front_img)
    canvas.itemconfig(my_title, fill="black")
    canvas.itemconfig(my_word, fill="black")
    word = random.choice(WORDS_DATA)
    CURRENT_WORD = word
    language = random.choice(list(word.keys()))
    canvas.itemconfig(my_title, text=language)
    canvas.itemconfig(my_word, text=word[language])
    CARD_TIMER = my_screen.after(3000, rotate_card, word, language)

def rotate_card(word, first_language):
    for language, word in word.items():
        if  first_language != language:
            canvas.itemconfig(my_card, image=card_back_img)
            canvas.itemconfig(my_title, fill="white")
            canvas.itemconfig(my_word, fill="white")
            canvas.itemconfig(my_title, text=language)
            canvas.itemconfig(my_word, text=word)

# -------------------------------------- UI CONFIG -------------------------------------- #
my_screen = Tk()
my_screen.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# IMG definition
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

#BUTTONS definition
wrong_btn = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, command=get_random_word)
right_btn = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, command=update_database)

#CANVAS definition
canvas = Canvas(width=800,height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
my_card = canvas.create_image(403, 268, image=card_front_img)
my_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
my_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")

#ELEMENTS grid
wrong_btn.grid(row=2, column=1)
right_btn.grid(row=2, column=2)
canvas.grid(row=1, column=1, columnspan=2)

get_data_from_file()
get_random_word()
save_data_to_file(WORDS_DATA)

my_screen.mainloop()