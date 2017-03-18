# -*- coding: UTF-8 -*-
from Tkinter import *
root = Tk()
root.wm_title("无监督高维数据变换与分类系统V1.0")#主界面名字
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
l1 = Label(root , text = "分类图像").grid(row = 0, column = 0)
l2 = Label(root , text = "降维算法").grid(row = 0, column = 4)
l3 = Label(root , text = "分类结果").grid(row = 1, column = 0)
l4 = Label(root , text = "聚类算法").grid(row = 1, column = 1)
l5 = Label(root , text = "算法性能").grid(row = 2, column = 0)
root.mainloop()