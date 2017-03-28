# -*- coding: UTF-8 -*-‘
#聚类算法暂时使用k-means
from sklearn.cluster import KMeans , AffinityPropagation , MeanShift , estimate_bandwidth , SpectralClustering
from sklearn.cluster import AgglomerativeClustering
def myKmeans(data,clusters):
    K_Means = KMeans(n_clusters=clusters, random_state=0, init='k-means++')
    result = K_Means.fit(data)
    reLabel = result.labels_
    return reLabel
def myAffinityPropagation(data,clusters):
    affinitypropagation = AffinityPropagation(damping=clusters, copy=True)
    result = affinitypropagation.fit(data)
    reLabel = result.labels_
    return reLabel
#这个算法效果很差劲，暂时不知道为啥
def myMeanShift(data,ckusters):
    bandwidth = estimate_bandwidth(data, quantile=0.9)
    meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    result = meanshift.fit(data)
    reLabel = result.labels_
    return reLabel
#def mySpectralClustering(data,clusters):
#    return reLabel
def myAgglomerativeClustering(data,clusters):
    agglomerativeclustering = AgglomerativeClustering(n_clusters=clusters, connectivity="array-like")
    result = agglomerativeclustering.fit(data)
    reLabel = result.labels_
    return reLabel