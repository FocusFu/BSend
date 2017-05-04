# -*- coding: UTF-8 -*-
'''
这个用来展示图片
'''
import transGif
from Tkinter import *
from ttk import *


def displaypic(root, command, list, label):
    if command == 0:
        line = 2
        for i in xrange(len(list)):
            if i < 9:
                label = Label(root, image=list[i]).grid(row=line, column=i, rowspan=3)
            elif i < 18:
                label = Label(root, image=list[i]).grid(row=line + 3, column=i - 9, rowspan=3)
            else:
                pass
    else:
        max = 0
        for i in xrange(len(label)):
            if max < label[i]:
                max = label[i]
        newlist = []
        newlabel = []
        for i in xrange(max+1):
            for j in xrange(len(list)):
                if label[j] == i:
                    newlist.append(list[j])
                    newlabel.append(label[j])
        list = newlist
        label = newlabel
        line = 10
        for i in xrange(len(list)):
            aa = 0#chr(label[i])
            if i < 9:
                label = Label(root, image=list[i], text=aa, compound="center")\
                    .grid(row=line, column=i, rowspan=3)
            elif i < 18:
                label = Label(root, text=aa, image=list[i], compound="center")\
                    .grid(row=line + 3, column=i - 9, rowspan=3)
            elif i < 27:
                label = Label(root, text=aa, image=list[i], compound="center")\
                    .grid(row=line + 6, column=i - 18, rowspan=3)
            else:
                pass

