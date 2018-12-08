# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-07 16:52:15
# @FileName:      opencv_image_initial.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-07 17:15:16
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('01-27-30.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
