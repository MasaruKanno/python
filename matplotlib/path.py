#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

verts = [[0, 0], [0.5, 0], [1, 0], [0, 0.5], [0.5, 0.5], [1, 0.5] , [0, 1], [0.5, 1], [1, 1]]
codes = [1, 1, 1, 1, 1, 1, 2, 2, 2]

path = Path(verts, codes)
cleaned_path = path.cleaned(simplify=True)

patch = mpatches.PathPatch(cleaned_path)
plt.plot(np.asarray(verts)[:, 0], np.asarray(verts)[:, 1], "rx")

ax.add_patch(patch)
plt.show()


# In[ ]:




