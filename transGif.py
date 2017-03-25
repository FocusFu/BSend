# -*- coding: UTF-8 -*-
'''
把要显示的图片转化为64*64
大概是一列三行
把要显示的图片转换为GIF
'''
from PIL import Image
def transPic(list):
    outlist = []
    for i in list:
        infile = 'test2\\' + i
        outfile = 'test2\\' + i[:-4] + '.gif'
        outlist.append(outfile)
        im = Image.open(infile)
        out = im.resize((64,64),Image.ANTIALIAS)
        out.save(outfile)
    return outlist
'''
infile = 'E:\obj1__0.png'
outfile = 'E:\obj.png'
im = Image.open(infile)
out = im.resize((64,64),Image.ANTIALIAS)
out.save(outfile)
im = Image.open('E:\obj.png')
im.save('E:\obj.gif')
'''