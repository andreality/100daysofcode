from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0)

language_text = canvas.create_text(400, 150, text="German", fill="white", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Einladung", fill="white", font=WORD_FONT)

button = Button(image=card_front_image, highlightthickness=0, bg=BACKGROUND_COLOR)
window.mainloop()
