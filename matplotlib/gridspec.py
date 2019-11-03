#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec

arr = [0, 1, 2, 3, 4, 5, 6] 
figure = plt.figure(figsize=(10, 5))

# レイアウト枠設定(5行3列)
p_nrows=5
p_ncols=3
gs_master = GridSpec(nrows=p_nrows, ncols=p_ncols, height_ratios=[1, 1, 1, 1, 1])
# 1列目
gs_1 = GridSpecFromSubplotSpec(nrows=p_nrows, ncols=1, subplot_spec=gs_master[0:5, 0])
axes_1 = figure.add_subplot(gs_1[:, :])
axes_1.plot(arr)
# 2列目
gs_2_3_4 = GridSpecFromSubplotSpec(nrows=p_nrows, ncols=2, subplot_spec=gs_master[0:5, 1])
axes_2 = figure.add_subplot(gs_2_3_4[1, :])
axes_3 = figure.add_subplot(gs_2_3_4[2, :])
axes_4 = figure.add_subplot(gs_2_3_4[3, :])
axes_2.plot(arr)
axes_3.plot(arr)
axes_4.plot(arr)
# 3列目
gs_5= GridSpecFromSubplotSpec(nrows=p_nrows, ncols=3, subplot_spec=gs_master[0:5, 2])
axes_5 = figure.add_subplot(gs_5[2, :])
axes_5.plot(arr)

plt.show()


# In[ ]:




