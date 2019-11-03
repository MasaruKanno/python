#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections

x = np.array([0,1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6,7])

fig = plt.figure()
fig_subplot = fig.add_subplot(111)

fig_subplot.plot(x, y, color='black')

# y軸の値が5以下は赤塗
p_ymin=1
p_ymax=7
p_where=y<=5
p_facecolor='red'
p_alpha=0.5
collection = collections.BrokenBarHCollection.span_where(x, ymin=p_ymin, ymax=p_ymax, where=p_where, facecolor=p_facecolor, alpha=p_alpha)
fig_subplot.add_collection(collection)

# y軸の値が3以上は青塗
p_where=y>=3
p_facecolor='blue'
collection = collections.BrokenBarHCollection.span_where(x, ymin=p_ymin, ymax=p_ymax, where=p_where, facecolor=p_facecolor, alpha=p_alpha)
fig_subplot.add_collection(collection)

# y軸の値が3～5は重なるため紫塗となる
fig.show()


# In[ ]:




