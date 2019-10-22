#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.font_manager as fm
import pandas as pd

serch_str = 'Mi' # 検索文字列

arr = []
for fname in fm.findSystemFonts():
    font = fm.FontProperties(fname=fname)
    arr.append(font.get_name())
dt_fm = pd.DataFrame(arr, columns=['NAME'])
dt_fm[dt_fm['NAME'].apply(lambda s: serch_str in s)]


# In[ ]:




