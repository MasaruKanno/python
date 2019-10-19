#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn
import pandas as pd
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# irisのデータを用意
iris = datasets.load_iris()
# 説明変数
data_x = iris.data
# 目的変数(アヤメの3品種(Setosa, Versicolour, Virginica))
data_y = iris.target

# 訓練、テストデータ取得
train_x,test_x,train_y,test_y = train_test_split(data_x,data_y)

# ロジスティック回帰の識別器を用意
clf = linear_model.LogisticRegression()

# 識別器を学習させる
clf.fit(train_x, train_y)

# テストデータで識別結果(正解率)を確認
print(clf.score(test_x, test_y))


# In[ ]:




