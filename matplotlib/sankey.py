#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Sanky Diagram")
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=[1.0, -0.3, -0.1, -0.1, -0.5],
           labels=['yamanote', 'keihinn', 'nannboku', 'syounann', ''],
           label='Tokyo Station',
           orientations=[0, -1, 1, 1, 0])
sankey.add(flows=[0.5, 0.1, 0.1, -0.1, -0.1, -0.1, -0.1, -0.3], fc='#37c959',
           label='Sinnzyuku Station',
           labels=['yamanote', 'hukutosinn', 'marunouchi', 'odakyuu', 'sinnzyuku','keiou', 'saikyou', 'chyuuou'],
           orientations=[0, -1, -1, 1, 1, -1, -1, 0], prior=0, connect=(4, 0))
diagrams = sankey.finish()
plt.legend(loc='upper center')
plt.axis('scaled')
plt.show()


# In[ ]:




