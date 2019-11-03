#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.transforms as transforms
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

trans = transforms.blended_transform_factory(
    ax.transData, ax.transAxes)

ax.plot(range(50))
ax.axvline(20)

ax.text(20, 0.15, 'test', transform=trans, rotation='vertical', ha='right')


# In[ ]:




