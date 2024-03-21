from tkinter import *


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# label
label = Label(text="I is a label!")
label.pack()


def button_clicked():
    label.config(text=input.get())


button = Button(text="Press me!", command=button_clicked)
button.pack()


input = Entry(width=10)
input.pack()


window.mainloop()
