# -*- coding: UTF-8 -*-
# This is a python file which include GUI codes
import time                   #引入时间模块
from Tkinter import *           # 导入 Tkinter 库
def xinlabel(event):
    global root
    s = Label(root , text = "aaaa")
    s.pack()
root = Tk()                    # 主界面
root.wm_title("无监督高维数据变换与分类系统V1.0")#主界面名字
#*******************************************************8
#菜单
menubar = Menu(root)
#for item in ['文件' , '帮助' , '说明']:
#    menubar.add_command(label = item)
amenu = Menu(menubar)
for item in ['打开' ,'保存']:
    amenu.add_command(label = item)
bmenu = Menu(menubar)
for item in ['降维算法' , '聚类算法']:
    bmenu.add_command(label = item)
menubar.add_cascade(label = "文件", menu = amenu)
menubar.add_cascade(label = "帮助", menu = bmenu)
menubar.add_cascade(label = "信息")
root['menu'] = menubar
#*************************************************************8
l1 = Label(root , text = "输入图片").grid(row = 0)
#b1 = Button(root , text = "PCA",command = xinlabel)
b1 = Button(root , text = "PCA")
b1.bind("<Button-1>",xinlabel)
#l1.pack()
b1.pack()
root.mainloop()                 # 进入消息循环