#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# データセット読み込み
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
x = iris.data
y = iris.target

# 学習データとテストデータに分割
x_train, x_test, y_train, y_test = train_test_split(x, y)

# ランダムフォレストのモデル構築
# n_jobs : 全てのコアを使用(-1)
# n_estimators : 使用する決定木数(デフォルト10)
model = RandomForestClassifier(n_estimators=20,n_jobs=-1)
model.fit(x_train, y_train)

#特徴量の重要度
feature = model.feature_importances_
#特徴量の名前
label = df.columns[0:]
#特徴量の重要度順(降順)
indices = np.argsort(feature)[::1]

# プロット
x = range(len(feature))
y = feature[indices]
y_label = label[indices]
plt.barh(x, y, align = 'center')
plt.yticks(x, y_label)
plt.xlabel("importance_num")
plt.ylabel("label")
plt.show()


# In[ ]:




