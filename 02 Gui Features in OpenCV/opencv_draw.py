# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-07 09:47:56
# @FileName:      opencv_draw.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-07 10:05:32
import numpy as np
import cv2 as cv

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# draw a diagonal blue line with thickness of 5px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv.rectangle(img, (5, 5), (506, 506), (0, 255, 0), 3)

cv.circle(img, (255, 255), 220, (0, 0, 255), -1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('image', img)
cv.waitKey(0)
