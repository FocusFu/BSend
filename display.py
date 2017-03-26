# -*- coding: UTF-8 -*-
'''
这个用来展示图片
'''
import transGif
from Tkinter import *
from ttk import *
def displaypic(root, command, list):
    if command == 0:
        line = 2
    else:
        line = 13
    for i in xrange(len(list)):
        if i < 9:
            label = Label(root, image=list[i]).grid(row = line, column = i, rowspan = 3)
        elif i < 18:
            label = Label(root, image=list[i]).grid(row=line+3, column=i-9, rowspan=3)
        else:
            label = Label(root, image=list[i]).grid(row=line+6, column=i-18, rowspan=3)
