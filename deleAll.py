# -*- coding: UTF-8 -*-
'''
删除某个格式的所有文件
file_ext--------'.gif'
file_address-------'E:\new'
'''
import os, re
def CleanAll(file_ext, file_address):
    # remove all files in bin
    for root, dirs, files in os.walk(file_address):
        for each_file in files:
            try:
                os.chdir(file_address)
                os.remove(each_file)
                os.chdir('../')
            except:
                pass
    # remove all object files in source foulder
    for root, dirs, files in os.walk('./'):
        pwd = os.getcwd()
        os.chdir(root)
        object_file_list = [f for f in os.listdir('.') if f.endswith(file_ext)]
        for file in object_file_list:
            os.remove(file)
        os.chdir(pwd)
CleanAll('.gif', 'D:\BSend\test2')