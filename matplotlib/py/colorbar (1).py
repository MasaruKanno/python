#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

x = np.arange(10)
y = np.arange(10)
X, Y = np.meshgrid(x, y)
Z = X**2. + Y**2.

fig = plt.figure()
ax1 = fig.add_subplot(111)
im = ax1.imshow(Z, interpolation='none') 
fig.colorbar(im)

# 色彩と境目表現について変更
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
im2 = ax2.imshow(Z, cmap=get_cmap('jet'), interpolation='hermite') 
fig2.colorbar(im2)

fig.show()


# In[ ]:




