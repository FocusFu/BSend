# -*- coding: UTF-8 -*-
#画坐标系
from Tkinter import *
from ttk import *
def biaogeH(root):
    for i in range(13):
        ll1 = Label(root, text=i, width=11).grid(row=0, column=i)
    for i in range(1, 27):
        ll1 = Button(root, text=i, width=11).grid(row=i, column=12)