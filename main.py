# -*- coding: UTF-8 -*-
# This is a python file which include GUI codes
import time                   #引入时间模块
from Tkinter import *           # 导入 Tkinter 库
root = Tk()
can = Canvas(root ,width = 400, height = 300)
can.create_line((0,0),(0,200), width = 2)
can.create_line((0,0),(200,0), width = 2)
can.create_line((200,0),(200,200), width = 2)
can.create_line((0,200),(200,200), width = 2)
can.pack()
root.mainloop()