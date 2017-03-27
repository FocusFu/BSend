# -*- coding: UTF-8 -*-
from Tkinter import *
from ttk import *
import tkFileDialog
import tkMessageBox
import transGif
from biaoge import *
import openPic
import display
import range
import randpic
import rd
from timeit import *
def timing():#测试时间
    pass
def opePic(nameList):#打开图片
    global dataList, addressList,dislist
    dislist = []
    dataList, addressList = openPic.openPictures(nameList)
    aaalist = randpic.randim(addressList)
    aaalist = transGif.transPic(aaalist)
    for i in xrange(len(aaalist)):
        dislist.append(PhotoImage(file = aaalist[i]))
    display.displaypic(root, 0, dislist)
def autherInf():
    tkMessageBox.showinfo("作者信息", "作者：符志强\r学号：13212002")
def selectPic():#选择要进行分类的图片
    filename = tkFileDialog.askopenfilename(initialdir='D:\BS\Caltech101')
    return filename
def bpcab(w, datalist, s):
    f = []
    aa = []
    bb = []
    #dataList, reData = rd.myPCA(datalist, s)
    for i in xrange(len(datalist)):
        aa, bb == rd.myPCA(datalist[i], s)
        f.append(aa)
    dataList = f
    print "ok"
    w.destroy()
def pcabut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    #w.resizable(width=0, height=0)
    e = IntVar()#StringVar()
    ln = Label(w, text="保留维数：").grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e).grid(row=0, column=1, sticky=E)
    s = e.get()
    bb = Button(w, text="确认", command=lambda: bpcab(w, datalist, s)).grid(row=1, column=1, sticky=E)

global imageData
global reData
global rlabel
global cc
rlabel = []
imageData = []
rowNumber = 1#起始行标
columnNumber = 0#起始列标
dataList = []
addressList = []
root = Tk()
root.wm_title("无监督高维数据变换与分类系统V1.0")#主界面名字
#root.wm_state( 'zoomed' )
root.geometry('1000x600+100+50')
root.resizable(width = 0, height = 0)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "打开",command = selectPic)
filemenu.add_command(label= "测试", command= lambda :opePic('test2/'))
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)
messagemenu = Menu(menubar, tearoff = 0)
messagemenu.add_command(label = "说明")
messagemenu.add_command(label = "作者", command = autherInf)
menubar.add_cascade(label = "信息", menu = messagemenu)
root['menu'] = menubar
biaogeH(root)
l1 = Label(root, text="分类图像").grid(row = rowNumber, column = columnNumber)
l2 = Label(root, text="降维算法").grid(row = rowNumber, column = columnNumber + 10)
b1 = Button(root, text="PCA", width=22, command=lambda: pcabut(root, dataList)).grid(row=rowNumber + 1, column=columnNumber + 10, columnspan=2)
b2 = Button(root, text="IncrementalPCA", width=22).grid(row = rowNumber + 2, column=columnNumber + 10, columnspan = 2)
b3 = Button(root, text="KernelPCA", width=22).grid(row=rowNumber + 3, column=columnNumber + 10, columnspan = 2)
l3 = Label(root, text="分类结果").grid(row = rowNumber + 10, column = columnNumber)
l4 = Label(root, text="聚类算法").grid(row = rowNumber + 4, column = columnNumber + 10)
b4 = Button(root, text="Kmeans", width = 22).grid(row=rowNumber + 5, column = columnNumber + 10, columnspan = 2)
b5 = Button(root, text="AffinityPropagation", width=22).grid(row = rowNumber + 6, column = columnNumber + 10, columnspan = 2)
b6 = Button(root, text="AgglomerativeClustering", width = 22).grid(row = rowNumber + 7, column = columnNumber + 10, columnspan = 2)
l5 = Label(root, text="算法性能").grid(row = rowNumber + 21, column = columnNumber)
l6 = Label(root, text="降维算法：").grid(row = rowNumber + 21, column = columnNumber)
lname = Label(root).grid(row = rowNumber + 21, column = columnNumber + 1)
l7 = Label(root, text="保留维数：").grid(row = rowNumber + 22, column = columnNumber)
ld = Label(root).grid(row = rowNumber + 22, column =columnNumber + 1)
l8 = Label(root, text="时间：").grid(row = rowNumber + 22, column = columnNumber + 2)
lt = Label(root).grid(row = rowNumber + 22, column = columnNumber +3)
l9 = Label(root, text="聚类算法：").grid(row = rowNumber + 23, column = columnNumber)
lname2 = Label(root).grid(row = rowNumber + 23, column = columnNumber +1)
l10 = Label(root , text = "准确率：").grid(row = rowNumber + 24, column = columnNumber)
text1 = Label(root, width = 11).grid(row = rowNumber + 24, column = columnNumber + 1)
l11 = Label(root , text="时间：").grid(row = rowNumber + 24, column = columnNumber + 2)
text2 = Label(root, width=11).grid(row=rowNumber + 24, column=columnNumber + 3)
root.mainloop()
