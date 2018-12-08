# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-06 17:16:41
# @FileName:      fetch_color.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-07 09:41:19

import cv2
import tkinter as tk
# import PIL.Image as Image


def main():
    global img

    img = cv2.imread('01-27-30.png', cv2.IMREAD_GRAYSCALE)
    # gui
    app = tk.Tk()
    app.title('Function')
    btn = tk.Button(app, text='显示图片', fg='blue', command=btn_view)
    btn.pack()
    btn2 = tk.Button(app, text='获取颜色', fg='blue', command=btn_get)
    btn2.pack()
    app.mainloop()

    # cv2
    cv2.waitKey(0)


def btn_view():
    global img
    btn_close()
    size = img.shape
    tmp = cv2.resize(img, (size[1] // 4, size[0] // 4), cv2.INTER_LINEAR)
    cv2.imshow('Show Image', tmp)


def btn_close():
    global img
    cv2.destroyAllWindows()


def btn_get():
    global img
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(hsv)
    btn_view()


if __name__ == '__main__':
    main()
