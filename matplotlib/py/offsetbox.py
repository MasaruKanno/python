#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.offsetbox as offsetbox

fig = plt.figure()
ax = fig.add_subplot(111)

text1 = '1\n'.format(0)
text2 = '2\n'.format(0)
text3 = '3'.format(0)
text = text1 + text2 + text3

ob = offsetbox.AnchoredText(text, loc=2, prop=dict(size=30))
ax.add_artist(ob)

plt.show()


# In[ ]:




