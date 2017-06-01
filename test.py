from rd import *
from PIL import Image
from scipy.misc import imread
img = Image.open('lenna.jpg')
im = imread('lenna.jpg')
re = myPCA(im, 0.99)
im.show()
img.show()