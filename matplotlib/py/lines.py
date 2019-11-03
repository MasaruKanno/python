#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
from matplotlib.lines import Line2D      

fig = plt.figure()
ax = fig.add_subplot(111)
# 座標(5,10),(1,5)・・・と線描画
x = [5,1,5,9,5]
y = [10,5,0,5,10]
line = Line2D(x, y)
ax.add_line(line)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()


# In[ ]:




