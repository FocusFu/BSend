# -*- coding: UTF-8 -*-
'''
这个用来打开图片,把所有的图片都放在test文件夹下
address----所在文件夹
'''
import os
from scipy.misc import imread
def getAllImages(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    imageList = os.listdir(folder)
    #imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return imageList
def openPictures(address):
    addressList = getAllImages(address)
    dataList = []
    for i in xrange(0 , len(addressList)):
        im = imread('test2/'+addressList[i])
        dataList.append(im.T)
    return dataList, addressList