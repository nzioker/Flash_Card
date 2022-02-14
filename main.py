from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window['background'] = BACKGROUND_COLOR
window.config(padx=50, pady=50)

# Functions


def read_data():
    file = pd.read_csv("data/french_words.csv") # this is a dataframe
    new_file = file.to_dict()
    random_number = random.randint(0, len(new_file["French"]))
    french_word = new_file["French"][random_number]
    english_word = new_file["English"][random_number]

    main_canvas.itemconfig(title_text, text="French")
    main_canvas.itemconfig(title_word, text=french_word)


card_front = PhotoImage(file="images/card_front.png")
main_canvas = Canvas(width=800, height=526)
main_canvas.create_image(400, 263, image=card_front)
title_text = main_canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
title_word = main_canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
main_canvas.grid(column=2, row=2, columnspan=2)
main_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_back = PhotoImage(file="images/card_back.png")

red_cross = PhotoImage(file="images/wrong.png")
wrong = Button(image=red_cross, highlightthickness=0, command=read_data)
wrong.grid(column=2, row=3)
green_checkmark = PhotoImage(file="images/right.png")
right = Button(image=green_checkmark, highlightthickness=0, command=read_data)
right.grid(column=3, row=3)





window.mainloop()
