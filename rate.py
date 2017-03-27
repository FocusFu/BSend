# -*- coding: UTF-8 -*-
'''
用来处理准确率
'''
def truerate(namelist, label):
    maxnum = 0
    for i in len(label):
        if maxnum < label[i]:
            maxnum = label[i]
    pass