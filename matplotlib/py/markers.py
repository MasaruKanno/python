#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as mplt
from matplotlib.markers import CARETDOWN

data = [2.]*10
data2 = [1.]*10

mplt.plot(data, 'r-')
mplt.plot(data2, 'b-')
mplt.scatter(range(10), data, facecolor='r') # 上部
mplt.scatter(range(10), data2, marker=CARETDOWN, facecolor='b') # 下部

mplt.show()


# In[ ]:




