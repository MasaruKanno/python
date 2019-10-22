#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.legend as lgd

fig = plt.figure()

ax = fig.add_subplot(111)
arr = [1,2,3]
line = ax.plot(arr)

ax2 = fig.add_subplot(111)
arr2 = [2,3,4]
line2 = ax2.plot(arr2)

ax3 = fig.add_subplot(111)
arr3 = [3,4,5]
line3 = ax3.plot(arr3)

# 1つ目の凡例生成
leg1 = ax.legend(line, ["1"], ncol=1) 
# 2つ目の凡例を生成
leg2 = lgd.Legend(ax2, line2, ["2"], ncol=2) 
# 3つ目の凡例を生成
leg3 = lgd.Legend(ax3, line3, ["3"], ncol=3) 

# 1つ目の凡例に2つ目の凡例を追加
leg1._legend_box._children.append(leg2._legend_box._children[1])
# 1つ目の凡例に3つ目の凡例を追加
leg1._legend_box._children.append(leg3._legend_box._children[1])
# デフォルト中央寄せのため、左寄せ
leg1._legend_box.align="left" 

fig.show()


# In[ ]:




