#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.tri as tri
import matplotlib.pyplot as plt

#x=(0,1,2,0,1,2)
#y=(0,0,0,0,1,0)
x=(0,1,2,0,1,2,0,1,2,0,1,2,0,1,2)
y=(0,0,0,1,1,1,2,2,2,3,3,3,4,4,4)

triang = tri.Triangulation(x, y)
plt.triplot(triang)
plt.show()


# In[ ]:




