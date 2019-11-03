#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib.cbook import flatten
l = (('John', ['Hunter']), (1, 23), [[([42, (5, 23)], )]])
print(l) # 平坦化前
print(list(flatten(l))) # 平坦化後


# In[ ]:




