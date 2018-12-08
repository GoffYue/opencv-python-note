# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-07 18:23:47
# @FileName:      opencv_image_core.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-08 13:12:15
import cv2 as cv
import numpy as np


# Mouse events Callback Function
def callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)


# Loading image
img = cv.imread('01-27-30.png')

# Accessing and Modifying pixel value
px = img[100, 100]
print('px: ', px)

blue = img[100, 100, 0]
print('px blue: ', blue)

img[100, 100] = [255, 255, 255]
print('px modify: ', img[100, 100])

it = img.item(10, 10, 2)
print('item: ', it)

# Accessing Image Properties
print('shape: ', img.shape)
print('size: ', img.size)
print('data type: ', img.dtype)
print('dir : ', dir(img))

# Modifying Image Properties
size = img.shape
img = cv.resize(img, (size[1] // 4, size[0] // 4), cv.INTER_LINEAR)

# Image ROI(Region of Interest) img[y:y+height, x:x+height]
crop_img = img[212:251, 699:740]
img[324:363, 597:638] = crop_img

# Splitting and Merging Image Channels
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

# or
b = img[:, :, 0], g = img[:, :, 1], r = img[:, :, 2]

# seting channel value
img[:, :, 2] = 0


cv.namedWindow('image')
cv.setMouseCallback('image', callback)

cv.imshow('image', img)
cv.waitKey(0)
