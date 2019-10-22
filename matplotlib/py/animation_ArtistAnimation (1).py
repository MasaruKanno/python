#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""
たけのこ成長記録
"""
# Jupyter上でアニメーションが再生可能にするため、matplotlibのnbaggを有効
get_ipython().run_line_magic('matplotlib', 'nbagg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure() #　表作成
plt.xlim(0, 6) #　x軸の範囲
plt.ylim(0, 10) #　y軸の範囲

ims = [] # グラフ描画配列
arr = [0, 0, 0, 0, 0, 0, 0] # グラフ配列初期値

for i in range(11): # i = 0～10までループ
    arr[3] = i # 成長具合
    im = plt.plot(arr) # 成長記録のプロット取得
    ims.append(im) # グラフ描画配列に追加

# 11枚のプロット(成長記録)を 300ms ごとにアニメーション表示
ani = animation.ArtistAnimation(fig, ims, interval=300)

ani.save("img/animation_ArtistAnimation.gif", writer="imagemagick") #カレントディレクトリにGIFファイル出力
plt.show()


# In[ ]:




