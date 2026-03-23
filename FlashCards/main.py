import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
timer = None
selected_card = {}

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/french_words.csv")
finally:
    words_list = words_data.to_dict(orient="records")


def flip_card():
    global timer, selected_card
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(lang_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=f"{selected_card['English']}")
    window.after_cancel(timer)


def next_card():
    global timer, selected_card
    window.after_cancel(timer)
    selected_card = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(lang_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=f"{selected_card['French']}")
    timer = window.after(3000, flip_card)


def remove_card():
    global selected_card
    words_list.remove(selected_card)
    remaining_data = pandas.DataFrame(data=words_list)
    remaining_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(width=900, height=900, padx=20, pady=20, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
lang_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

tick_img = PhotoImage(file="images/right.png")
correct_button = Button(image=tick_img, highlightthickness=0, command=remove_card)
correct_button.grid(row=1, column=1)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
