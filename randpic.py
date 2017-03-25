# -*- coding: UTF-8 -*-
'''
这个用来取出随机数
'''
import random
def randim(list):
    display = []
    a = len(list)
    randnumber = [random.randint(0, a - 1) for _ in range(27)]
    for i in xrange(27):
        display.append(list[randnumber[i]])
    return display