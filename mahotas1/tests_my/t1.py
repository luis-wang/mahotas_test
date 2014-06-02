#coding:utf8
'''

'''
import numpy as np
import mahotas
import pylab

img = mahotas.imread('test.jpeg')
T_otsu = mahotas.thresholding.otsu(img)
seeds,_ = mahotas.label(img > T_otsu)
labeled = mahotas.cwatershed(img.max() - img, seeds)


