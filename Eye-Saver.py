import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import pygame as pg

NUMBER = 20
HIDE_TIME = 60 * 20
FIRST_TIME = 60 * 10
BG_COLOR = "#151922"


root = Tk()
root.geometry("1800x1000")
root.title('Eye Saver')
root.configure(bg= BG_COLOR)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 0)
root.columnconfigure(2, weight = 1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 0)
root.rowconfigure(2, weight = 0)
root.rowconfigure(3, weight = 0)
root.rowconfigure(4, weight = 1)

pg.mixer.init()
sound = pg.mixer.Sound('C:/Users/harve/Desktop/Length Function, basics/Monthly cashflow/Eye-Saver/Blank Canvas.wav')

def show_window():
    root.deiconify()
    sound.play()
    update()

def first():
    root.deiconify()
    update()

def remove():
    title.grid_remove()
    text.grid_remove()
    button.grid_remove()
    countdown_text.grid(column= 1, row = 2)
    countdown_number.grid(column=1, row=3, pady = 160)
    root.withdraw()
    root.after(FIRST_TIME * 1000)
    sound.play()
    first()

def update():
    global NUMBER
    if NUMBER > 0:
        countdown_number.config(text = str(NUMBER))
        NUMBER -= 1
        countdown_number.after(1000, update)
    else:
        root.withdraw()
        NUMBER = 20
        root.after(HIDE_TIME * 1000, show_window)

import Fonts

title = tk.Label(text = "Eye Saver", fg = "white", bg = BG_COLOR, font = Fonts.title_font)
title.size = (40, 20)
title.grid(column=1, row=1, pady=80)

text = tk.Label(text = "This program will remind you every 20 minutes to look away for the health of your eyes!", fg = "white", bg = BG_COLOR, font = Fonts.text_font)
text.grid(column=1, row=2, pady=30)

button = tk.Button(text = "Start", command = remove, fg = "white", bg = BG_COLOR, font = Fonts.button_font)
button.grid(column=1, row=3, pady = 140)

countdown_number = tk.Label(text = str(NUMBER),  fg = "white", bg = BG_COLOR, font = Fonts.countdown_font)
countdown_text = tk.Label(text = "Look at something roughly 6 meters away or fruther", fg = "white", bg = BG_COLOR, font = Fonts.countdown_text_font)


root.mainloop()
