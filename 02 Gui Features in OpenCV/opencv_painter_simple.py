# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-07 13:03:33
# @FileName:      opencv_painter.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-07 13:16:18
import cv2 as cv
import numpy as np


# mouse callback function
def draw_circle(event, x, y, flags, param):
    print(x, y)
    if event == cv.EVENT_MOUSEMOVE:
        cv.circle(img, (x, y), 2, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
