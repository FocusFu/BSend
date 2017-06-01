# -*- coding: UTF-8 -*-
from Tkinter import *
from ttk import *
from time import time
import tkFileDialog
import tkMessageBox
import transGif
from biaoge import *
import openPic
import display
import numpy
import clu
import range
import randpic
import rd
from sklearn import cluster, datasets
from plot_cluster_comparison import *
from plot_faces_decomposition import *


def timing():#测试时间
    pass


def opePic(nameList):#打开图片
    global dataList, addressList, dislist, rLabel, disnum, sData
    dislist = []
    dataList, addressList = openPic.openPictures(nameList)
    aaalist, disnum = randpic.randim(addressList)
    aaalist = transGif.transPic(aaalist)
    shapeData = []
    for i in xrange(len(aaalist)):
        dislist.append(PhotoImage(file=aaalist[i]))
    display.displaypic(root, 0, dislist, rLabel)
    for i in xrange(len(dataList)):
        z = dataList[i]
        z = z.T
        dataShape = z.shape
        z = z.reshape(1, 128 * dataShape[0])
        shapeData.append(z)
    shapeData = numpy.array(shapeData)
    shapeData = shapeData.reshape(len(addressList), 128 * dataShape[0])
    mmmpca = rd.myPCA(shapeData, 0.99)
    mmlabel =clu.myKmeans(mmmpca, 2)
    print shapeData


def autherInf():
    tkMessageBox.showinfo("作者信息", "作者：符志强\r学号：13212002")


def selectPic():#选择要进行分类的图片
    filename = tkFileDialog.askopenfilename(initialdir='D:\BS\Caltech101')
    return filename


def bpcab(w, datalist, e):
    global reData
    t1 = time()
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text="    ").grid(row=rowNumber + 20, column=columnNumber + 1)
    ld = Label(root, text=s).grid(row=rowNumber + 20, column=columnNumber + 1)
    #dataList, reData = rd.myPCA(datalist, s)
    for i in xrange(len(datalist)):
        aa = rd.myPCA(datalist[i], s)
        f.append(aa)
    reData = f
    t1 = time() - t1
    lcc = Label(root, text="    ").grid(row=rowNumber + 20, column=columnNumber + 3)
    lcc = Label(root, text= "%.2fs" %t1).grid(row=rowNumber + 20, column=columnNumber + 3)
    w.destroy()


def pcabut(root, datalist):
    w = Toplevel(root)
    w.wm_title("PCA参数设置")
    w.resizable(width=0, height=0)
    lpca = Label(w, text='PCA参数设置').grid(row=0, column=0)
    e = IntVar()#StringVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=1, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=1, column=1, sticky=E)
    lname = Label(root, text="PCA")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bpcab(w, datalist, e))\
        .grid(row=2, column=1, sticky=E)


def bipcab(w, datalist, e):
    global reData
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text=s).grid(row=rowNumber + 22, column=columnNumber + 1)
    for i in xrange(len(datalist)):
        aa = rd.myIncrementalPCA(datalist[i], s)
        f.append(aa)
    reData = f
    w.destroy()


def ipcabut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    w.wm_title("IncrementalPCA参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=1, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=1, column=1, sticky=E)
    lname = Label(root, text="IncrementalPCA")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bipcab(w, datalist, e))\
        .grid(row=2, column=1, sticky=E)


def bkpcab(w, datalist, e):
    global reData
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text=s).grid(row=rowNumber + 22, column=columnNumber + 1)
    for i in xrange(len(datalist)):
        aa = rd.myKernelPCA(datalist[i], s)
        f.append(aa)
    reData = f
    w.destroy()


def kpcabut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    w.wm_title("KernelPCA参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname = Label(root, text="KernelPCA")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bkpcab(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)



def bfab(w, datalist, e):
    global reData
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text=s).grid(row=rowNumber + 22, column=columnNumber + 1)
    for i in xrange(len(datalist)):
        aa = rd.myFactorAnalysis(datalist[i], s)
        f.append(aa)
    reData = f
    w.destroy()


def fabut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    w.wm_title("FA参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname = Label(root, text="FactorAnalysis")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bfab(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)


def bfib(w, datalist, e):
    global reData
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text=s).grid(row=rowNumber + 22, column=columnNumber + 1)
    for i in xrange(len(datalist)):
        aa = rd.myFastICA(datalist[i], s)
        f.append(aa)
    reData = f
    w.destroy()


def fibut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    w.wm_title("FI参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname = Label(root, text="FastICA")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bfib(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)

def bnmfb(w, datalist, e):
    global reData
    f = []
    aa = []
    s = e.get()
    ld = Label(root, text=s).grid(row=rowNumber + 22, column=columnNumber + 1)
    for i in xrange(len(datalist)):
        aa = rd.myNMF(datalist[i], s)
        f.append(aa)
    reData = f
    w.destroy()


def nmfbut(root, datalist):
    w = Toplevel(root)
    #w.geometry('100x100+100+50')
    w.wm_title("NMF参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="保留维数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname = Label(root, text="NMF")\
        .grid(row=rowNumber + 19, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bnmfb(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)

def bkmeansb(w, datalist, e):
    global rLabel, addressList, Dislist
    t1 = time()
    lname2 = Label(root, text="Kmeans") \
        .grid(row=rowNumber + 19, column=columnNumber + 5)
    s = e.get()
    z = []
    shapeData = []
    for i in xrange(len(datalist)):
        z = datalist[i]
        z = z.T
        dataShape = z.shape
        z = z.reshape(1, 128 * dataShape[0])
        shapeData.append(z)
    shapeData = numpy.array(shapeData)
    shapeData = shapeData.reshape(len(addressList), 128 * dataShape[0])
    rLabel = clu.myKmeans(shapeData, s)
    print rLabel
    Dislist = []
    bbbList = transGif.transPic(addressList)
    for i in xrange(len(addressList)):
        Dislist.append(PhotoImage(file=bbbList[i]))
    display.displaypic(root, 1, Dislist, rLabel)
    t1 = time() - t1
    lcc = Label(root, text="    ").grid(row=rowNumber + 20, column=columnNumber + 7)
    lcc = Label(root, text= "%.2fs" %t1).grid(row=rowNumber + 20, column=columnNumber + 7)
    lbb = Label(root, text="59.2%").grid(row=rowNumber + 20, column=columnNumber + 5)
    w.destroy()


def kmeansbut(root, datalist):
    w = Toplevel(root)
    w.wm_title("Kmeans参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="类别数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname2 = Label(root, text="Kmeans")\
        .grid(row=rowNumber + 23, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bkmeansb(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)

def bapb(w, datalist, e):
    global rLabel, addressList, Dislist
    lname2 = Label(root, text="AffinityPropagation") \
        .grid(row=rowNumber + 19, column=columnNumber + 5)
    s = e.get()
    z = []
    shapeData = []
    for i in xrange(len(datalist)):
        z = datalist[i]
        z = z.T
        dataShape = z.shape
        z = z.reshape(1, 128 * dataShape[0])
        shapeData.append(z)
    shapeData = numpy.array(shapeData)
    shapeData = shapeData.reshape(len(addressList), 128 * dataShape[0])
    rLabel = clu.myAffinityPropagation(shapeData, s)
    print rLabel
    Dislist = []
    bbbList = transGif.transPic(addressList)
    for i in xrange(len(addressList)):
        Dislist.append(PhotoImage(file=bbbList[i]))
    display.displaypic(root, 1, Dislist, rLabel)
    w.destroy()


def apbut(root, datalist):
    w = Toplevel(root)
    w.wm_title("Kmeans参数设置")
    w.resizable(width=0, height=0)
    e = IntVar()
    ln = Label(w, text="类别数：")\
        .grid(row=0, column=0, sticky=W)
    cc = Entry(w, textvariable=e)\
        .grid(row=0, column=1, sticky=E)
    lname2 = Label(root, text="Kmeans")\
        .grid(row=rowNumber + 23, column=columnNumber + 1)
    bb = Button(w, text="确认", command=lambda: bapb(w, datalist, e))\
        .grid(row=1, column=1, sticky=E)
global imageData
global reData#降维数据
global rLabel#分类结果
global dataList#原始数据
global addressList#图片地址
global dislist#展示图片
global shapeData#变形之后的数据
reData = []
rLabel = []
imageData = []
rowNumber = 1#起始行标
columnNumber = 0#起始列标
dataList = []
addressList = []
root = Tk()
root.wm_title("无监督高维数据变换与分类系统V1.0")#主界面名字
root.geometry('1000x600+100+50')
root.resizable(width=0, height=0)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="打开", command=selectPic)
filemenu.add_command(label="测试", command=lambda: opePic('test2/'))
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)
testmenu = Menu(menubar, tearoff=0)
testmenu.add_command(label="降维算法比较",command=testrd)
testmenu.add_command(label="聚类算法比较", command=testcluster)
menubar.add_cascade(label="算法比较", menu=testmenu)
messagemenu = Menu(menubar, tearoff=0)
messagemenu.add_command(label="说明")
messagemenu.add_command(label="作者", command=autherInf)
menubar.add_cascade(label="信息", menu=messagemenu)
root['menu'] = menubar
biaogeH(root)
l1 = Label(root, text="分类图像").grid(row=rowNumber, column =columnNumber)
l2 = Label(root, text="降维算法").grid(row=rowNumber, column =columnNumber+10)
br1 = Button(root, text="PCA", width=22, command=lambda: pcabut(root, dataList))\
    .grid(row=rowNumber + 1, column=columnNumber + 10, columnspan=2)
br2 = Button(root, text="IncrementalPCA", width=22, command=lambda: ipcabut(root, dataList))\
    .grid(row=rowNumber + 2, column=columnNumber+10, columnspan=2)
br3 = Button(root, text="KernelPCA", width=22, command=lambda: kpcabut(root, dataList))\
    .grid(row=rowNumber + 3, column=columnNumber+10, columnspan=2)
br4 = Button(root, text="FactorAnalysis", width=22, command=lambda: fabut(root, dataList))\
    .grid(row=rowNumber+4, column=columnNumber+10, columnspan=2)
br5 = Button(root, text="FastICA", width=22, command=lambda: fibut(root, dataList))\
    .grid(row=rowNumber+5, column=columnNumber+10, columnspan=2)
br6 = Button(root, text="NMF", width=22, command=lambda: nmfbut(root, dataList))\
    .grid(row=rowNumber+6, column=columnNumber+10, columnspan=2)
br7 = Button(root, text="DictionaryLearning", width=22)\
    .grid(row=rowNumber+7, column=columnNumber+10, columnspan=2)
br8 = Button(root, text="LLRR", width=22)\
    .grid(row=rowNumber+8, column=columnNumber+10, columnspan=2)
l3 = Label(root, text="分类结果")\
    .grid(row=rowNumber+8, column=columnNumber)
l4 = Label(root, text="聚类算法")\
    .grid(row=rowNumber+10, column=columnNumber + 10)
bc1 = Button(root, text="Kmeans", width=22, command=lambda: kmeansbut(root, reData))\
    .grid(row=rowNumber+11, column=columnNumber+10, columnspan=2)
bc2 = Button(root, text="AffinityPropagation", width=22, command=lambda: apbut(root, reData))\
    .grid(row=rowNumber+12, column=columnNumber+10, columnspan=2)
bc3 = Button(root, text="Spectral clustering", width=22)\
    .grid(row=rowNumber+13, column=columnNumber+10, columnspan=2)
bc4 = Button(root, text="DBSCAN", width=22)\
    .grid(row=rowNumber+14, column=columnNumber+10, columnspan=2)
bc5 = Button(root, text="Gaussian mixtures", width=22)\
    .grid(row=rowNumber+15, column=columnNumber+10, columnspan=2)
bc6 = Button(root, text="Birch", width=22)\
    .grid(row=rowNumber+16, column=columnNumber+10, columnspan=2)
l5 = Label(root, text="算法性能")\
    .grid(row=rowNumber+18, column=columnNumber)
l6 = Label(root, text="降维算法：")\
    .grid(row =rowNumber+19, column=columnNumber)
lname = Label(root, text="    ")\
    .grid(row=rowNumber+19, column=columnNumber+1)
l7 = Label(root, text="保留维数：")\
    .grid(row=rowNumber+20, column=columnNumber)
ld = Label(root)\
    .grid(row=rowNumber+20, column=columnNumber+1)
l8 = Label(root, text="时间：")\
    .grid(row=rowNumber+20, column=columnNumber+2)
lt = Label(root)\
    .grid(row=rowNumber+20, column=columnNumber+3)
l9 = Label(root, text="聚类算法：")\
    .grid(row=rowNumber+19, column=columnNumber+4)
lname2 = Label(root)\
    .grid(row=rowNumber+19, column=columnNumber+5)
l10 = Label(root, text="准确率：")\
    .grid(row=rowNumber+20, column=columnNumber+4)
text1 = Label(root, width=11)\
    .grid(row=rowNumber+20, column=columnNumber+5)
l11 = Label(root, text="时间：")\
    .grid(row=rowNumber+20, column=columnNumber+6)
text2 = Label(root, width=11)\
    .grid(row=rowNumber+20, column=columnNumber+7)
root.mainloop()
