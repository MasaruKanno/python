#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from matplotlib.text import Text

txt = Text(text='Text Display', x=0.4, y=0.5)

fig, ax = plt.subplots()
ax._set_artist_props(txt)
ax.texts.append(txt)

print(ax.texts)
plt.show()


# In[ ]:




