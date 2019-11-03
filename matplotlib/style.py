#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

arr = [0,1,2,3]
fig = plt.figure()
ax = fig.add_subplot(111)
style.use('ggplot')
ax.plot(arr)


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
arr = [0,1,2,3]

fig = plt.figure()
ax = fig.add_subplot(111)
style.use('classic')
ax.plot(arr)


# In[ ]:




