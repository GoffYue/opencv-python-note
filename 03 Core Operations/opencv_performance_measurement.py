# -*- coding: utf-8 -*-
# @Author:        Goff
# @Date:          2018-12-09 16:48:39
# @FileName:      opencv_performance_measurement.py
# @Description:

# @Last Modified by:   Goff_Wang
# @Last Modified time: 2018-12-10 12:45:22
import cv2 as cv


# Measuring Performance with OpenCV
e1 = cv.getTickCount()
pass  # your code execution
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print('time costs: ', t)  # return time(sec)

# Default Optimization in OpenCV
cv.useOptimized()  # return True of False
cv.setUseOptimized(False)  # Disable it

# %timeit (IPython)
# In[1]: %timeit res = cv.medianBlur(img, 49)

# Measuring Performance in IPython
# In[2]: x = 5
# In[3]: %timeit y = x**2
# In[4]: %timeit y = x * x  # better

# In[5]: z = np.uint8([5])
# In[6]: %timeit y = z * z
# In[7]: %timeit y = np.square(z)  # better

# In[8]: %timeit z = cv.countNonZero(img)  # better
# In[9]: %timeit z = np.count_nonzero(img)
