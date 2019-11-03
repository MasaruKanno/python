#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np

args = np.random.rand(5)
print (args)

# patheffects不使用
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(args, linewidth=4, color='r')

# patheffects使用
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(args, linewidth=4, color='r', path_effects=[
    path_effects.Stroke(linewidth=8, foreground='black'),
    path_effects.Normal()
    ])

plt.show()


# In[ ]:




