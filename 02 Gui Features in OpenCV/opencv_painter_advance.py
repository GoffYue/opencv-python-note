# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-07 13:17:49
# @FileName:      opencv_painter_advance.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-07 13:39:21
import cv2 as cv
import numpy as np

img = 0
drawing = False
mode = True
ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


def main():
    global img, mode
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_circle)

    while True:
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
