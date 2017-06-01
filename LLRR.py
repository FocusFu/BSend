from numpy import *

def mykNN(data, k):
    arSize = data.shape
    knnSave = zeros([arSize[0], k+1])
    dis = zeros([arSize[0], arSize[0]])
    for i in xrange(arSize[0]):
        for j in xrange(arSize[0]):
            dis[i, j] = linalg.norm(data[i] - data[j])
    for i in xrange(k+1):
        list = argmin(dis, 0)
        if i != 0:
            if i == k:
                for j in xrange(arSize[0]):
                    knnSave[j, i] = dis[j, list[j]]
            for j in xrange(arSize[0]):
                knnSave[j, i-1] = list[j]
                dis[j, list[j]] = 100000000
        else:
            dis[j, list[j]] = 100000000
            for j in xrange(arSize[0]):
                dis[j, list[j]] = 100000000
    return knnSave



def myLLRR(Y, k):
    Ysize = Y.shape
    lamda = 0.02
    beta = 1.0
    garma = 5.0
    M1 = 0
    M2 = 0
    rho0 = 2.5
    mu0 = 1e-6
    mumax = 1e+6
    tol1 = 1e-6
    tol2 = 1e-2
    eta = 0
    Z = zeros([Ysize[0],Ysize[0]])
    Ek = Zk = Jk = E = Z
    muk = rhok = 0
    knnr = mykNN(Y, k)
    W = zeros([Ysize[0], Ysize[0]])
    for i in xrange(Ysize[0]):
        for j in xrange(k):
            W[i, int(knnr[i, j])] = 1
            W[int(knnr[i, j]), i] = 1

    D = zeros([Ysize[0], Ysize[0]])
    L = D - W
    while(1):
        zqZ = beta*()



        if(linalg.det(Y-Y*Z-E)/linalg.det(Y) < tol1 and
                   max(eta*linalg.det(Zk-Z), muk*linalg.det(Jk-J),muk*linalg.det(Ek-E))<tol2):
            break

    print W

data = array([[1, 2, 3], [4, 5, 6]]);
myLLRR(data, 1)
