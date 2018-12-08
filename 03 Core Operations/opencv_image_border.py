# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-08 13:17:09
# @FileName:      opencv_image_border.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-08 16:54:36
import cv2 as cv
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

# better use absolute path
img = cv.imread("roi.png")

replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(
    img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
