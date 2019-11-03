#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
雨粒から水溜りへ
"""
get_ipython().run_line_magic('matplotlib', 'nbagg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure() #　表作成

def plot(data):
    x = np.random.randn(100) # X軸に100個の乱数
    y = x + np.random.randn(100)# Y軸に100個の乱数
    im = plt.plot(x, y, "b.") # 描画

# 300ms ごとにplot()結果をアニメーション表示
ani = animation.FuncAnimation(fig, plot, interval=300)
ani.save("img/animation_FuncAnimation.gif", writer="imagemagick") #カレントディレクトリにGIFファイル出力
plt.show()


# In[ ]:




