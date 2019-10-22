#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch

plt.plot((0, 0, 1, 1, 0), (1, 0, 0, 1, 1),color="gray")

tp = TextPath((0,0), "TextPath", size=0.2)
plt.gca().add_patch(PathPatch(tp, color="blue"))

plt.show()


# In[ ]:




