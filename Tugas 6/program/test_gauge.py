#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib

win = tk.Tk()
a5 = PhotoImage(file="1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Kimochii na")
win.geometry("500x200+0+0")
win.resizable(width=True, height=True)
win.configure(bg='black')

g_value=0
x=0

def read_every_second():
    global x    
    g_value=random.randint(0,100)
    p3.set_value(int(g_value))   
    x+=1    
    if x>100:
#        graph1.draw_axes()
        x=0
    win.after(100, read_every_second)

p3 = gaugelib.DrawGauge3(
    win,
    max_value=100.0,
    min_value= 0.0,
    size=201,
    bg_col='black',
    unit = "Km/H",bg_sel = 1)
p3.pack()

read_every_second()
mainloop()
