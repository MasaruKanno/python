#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker # FormatterとLocatorはTickerモジュールが必要

x = np.linspace(0, 2*np.pi, 100) # データ

# Figureクラス(グラフの箱を生成)
fig = plt.figure() 

# Axesクラス(グラフデータの描画を生成)
ax = fig.add_subplot(211) 
line1 = ax.plot(x, np.sin(x), label='1st plot') # 1つ目のAxes.lines
line2 = ax.plot(x, np.sin(x+np.pi/8), label='2nd plot') # 2つ目のAxes.lines
scat = ax.scatter(x, np.random.rand(len(x)), label='scatter') # 3つ目のAxes.collections


# Axisクラス(XY軸についての設定)
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=10))


# Tickクラス(書式設定等)
plt.tick_params(labelsize=18) # XY軸のラベルサイズを設定

fig.show()


# In[ ]:




