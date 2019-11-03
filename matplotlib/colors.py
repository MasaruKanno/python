#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

a = np.arange(10)
cmap = plt.get_cmap("tab10") # 色情報取得

for i in range(10):
    ax.plot(a,a+i, color=cmap(i))

plt.show()


# In[ ]:




