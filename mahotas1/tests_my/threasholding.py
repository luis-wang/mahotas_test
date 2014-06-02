#coding:utf8
'''

'''
import mahotas
import numpy as np
from pylab import imshow, gray, show, subplot
from os import path

photo = mahotas.imread('draw_on_img.png', as_grey=True)
photo = photo.astype(np.uint8)

T_otsu = mahotas.otsu(photo)
thresholded_otsu = (photo > T_otsu)

T_rc = mahotas.rc(photo)
thresholded_rc = (photo > T_rc)


