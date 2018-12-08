# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-08 17:11:20
# @FileName:      opencv_arithmetic_operations.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-08 22:20:05
import cv2 as cv
import numpy as np


# Image Addition
x = np.uint8([250])
y = np.uint8([10])

print('cv.add(): ', cv.add(x, y))
print('x+y: ', x + y)

# Image Blending
img_01 = cv.imread('blend01.jpg')
img_02 = cv.imread('blend02.jpg')
# dst = cv.addWeighted(img_01, 0.7, img_02, 0.3, 0)
dst = img_01 * 0.7 + img_02 * 0.3
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
