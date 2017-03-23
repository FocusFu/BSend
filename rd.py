# -*- coding: UTF-8 -*-
#这是主成分分析算法的一个模块，加一个归一化
#主成分分析和核主成分分析
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import KernelPCA
import numpy as np
def myPCA(data,percent):
    pca = PCA(n_components = percent,copy=True,whiten=False,svd_solver='auto')
    lowDData = np.array( pca.fit_transform(data))
    reDData = pca.inverse_transform(lowDData)
    maxData=np.max(lowDData,axis=0)
    minData=np.min(lowDData,axis=0)
    rangeData=maxData-minData
    lowDData=lowDData/rangeData
    return lowDData , reDData
def myIncrementalPCA(data,percent):
    incrementalpca = IncrementalPCA(n_components = percent, copy = True )
    lowDData = np.array( incrementalpca.fit_transform(data))
    reDData = incrementalpca.inverse_transform(lowDData)
    maxData=np.max(lowDData,axis=0)
    minData=np.min(lowDData,axis=0)
    rangeData=maxData-minData
    lowDData=lowDData/rangeData
    return lowDData , reDData
#核PCA参数比较复杂很麻烦，暂时只考虑一个内核
def myKernelPCA(data,percent):
    kernelpca = KernelPCA(n_components = percent,kernel = "poly")
    lowDData = np.array(kernelpca.fit_transform(data))
    reDData = kernelpca.inverse_transform(lowDData)
    maxData = np.max(lowDData, axis=0)
    minData = np.min(lowDData, axis=0)
    rangeData = maxData - minData
    lowDData = lowDData / rangeData
    return lowDData, reDData
def mySparsePCA(data,percent):
    pass