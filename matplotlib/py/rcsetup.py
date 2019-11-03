#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pylab as plt
import matplotlib.rcsetup as rcsetup
import numpy as np

# rc設定カスタマイズ前
jet = plt.cm.jet
fig, ax = plt.subplots()
N = 20
idx = np.linspace(0, 1, N)
x = np.linspace(0, 100, 200)
for i in range(1, N+1):
    ax.plot(x, np.sin(x)+i)

ax.set_ylim(0, N+1)

# rc設定カスタマイズ後
fig2, ax2 = plt.subplots()
ax2.set_prop_cycle(rcsetup.cycler('color', jet(idx)))
for i in range(1, N+1):
    ax2.plot(x, np.sin(x)+i)

ax2.set_ylim(0, N+1)

plt.show()


# In[ ]:




