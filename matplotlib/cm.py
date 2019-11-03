#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(nrows=7,sharex=True)

x =np.linspace(0,2*np.pi,100)
for i in range(30):   
    y=i*np.sin(x)
    ax1.plot(x, y, color=cm.rainbow(i/30.0))
    ax2.plot(x, y, color=cm.Reds(i/30.0))
    ax3.plot(x, y, color=cm.binary(i/30.0))
    ax4.plot(x, y, color=cm.PiYG(i/30.0))
    ax5.plot(x, y, color=cm.twilight(i/30.0))
    ax6.plot(x, y, color=cm.Pastel1(i/30.0))
    ax7.plot(x, y, color=cm.flag(i/30.0))

ax1.set_xlim(0, 2*np.pi)
fig.show()


# In[ ]:




