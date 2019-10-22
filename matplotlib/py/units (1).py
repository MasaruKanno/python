#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.units, matplotlib.dates
import datetime

# カスタムクラス
class CostomClass(datetime.datetime):
   def date_format(self):
     return '{1:02d}{2:02d}{3:02d}'.format(self.year, self.month, self.day)

matplotlib.units.registry[CostomClass] = matplotlib.dates.DateConverter()

# オリンピック開催期間
x = [CostomClass(2020, 7, 1), CostomClass(2020, 7, 10)]
y = [0, 1]
plt.xticks(rotation = 90)
plt.plot(x, y)


# In[ ]:




