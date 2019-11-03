#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from matplotlib import mathtext

mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants
#Hと2の間に違い
#mathtext.FontConstantsBase = mathtext.STIXSansFontConstants

plt.rcParams.update({'font.size': 18})

plt.text(0.5, 0.5, '$H_2O$', ha='center')

plt.show()


# In[ ]:




