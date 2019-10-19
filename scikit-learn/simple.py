#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston() # データセットの読み込み
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df['PRICE']=boston.target
boston_df.head()
y='PRICE' # 目的変数
x='RM'#説明変数
df = boston_df[[x,y]].corr()
# かなり強い相関(0.7～1)
# やや強い相関(0.4～0.7)
# 弱い相関(0.2～0.4)
# ほとんど相関なし(0.0～0.2)
df


# In[ ]:




