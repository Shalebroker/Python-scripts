#!/usr/bin/env python
# coding: utf-8

# Simple GUI (tkinter)

import tkinter as tk
from PIL import Image, ImageTk
import random

# main window of an application
root = tk.Tk()
root.geometry('400x400')
root.title('K6 dice roll')

# Adding label into the frame
l0 = tk.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tk.Label(root, text="Welcom to k6 dice roll", fg = "brown",
        bg = "yellow",
        font = "Helvetica 18 bold italic")
l1.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 1 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tk.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack( expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

# adding button, and command will use rolling_dice function
button = tk.Button(root, text='Roll k6 dice', fg='brown', command=rolling_dice)

# pack a widget in the parent widget
button.pack( expand=True)

# call the mainloop of Tk and keeps window open
root.mainloop()


# In[ ]:




