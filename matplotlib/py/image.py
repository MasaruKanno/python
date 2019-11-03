#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

fig = plt.figure()
ax =  fig.add_subplot(111)

# 画像読み込み(PNG)
img = mpimg.imread('img/matplotlib_image.png')
print("↓PNGの形式の画像読み書きはfloat32データ↓\r\n", img)
# 画像読み込み(PNG以外)
img = mpimg.imread('img/matplotlib_image.jpg')
print("↓PNG以外の形式の画像読み書きはuint8データ↓\r\n", img)

plt.imshow(img)


# In[ ]:




