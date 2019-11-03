#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches

circle = patches.CirclePolygon((0, 0), radius = 1, fc = 'b')
circle2 = patches.CirclePolygon((2, 0), radius = 1, fc = 'y')
circle3 = patches.CirclePolygon((4, 0), radius = 1, fc = 'r')
plt.gca().add_patch(circle)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle3)
plt.axis('scaled')
plt.show()


# In[ ]:




