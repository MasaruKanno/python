#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import pickle

dataset = load_boston()#データセット読み込み

data_x = pd.DataFrame(dataset.data,columns=dataset.feature_names)#説明変数
data_y = pd.DataFrame(dataset.target)#目的変数

#　クロスバリデーション法を使用
# 学習データ(train_)とテストデータ(test_)を作成
train_x,test_x,train_y,test_y = train_test_split(data_x,data_y)

#正規化インスタンス
mscaler = MinMaxScaler()
#訓練データの説明変数を正規化
mscaler.fit(train_x)#読み込み
train_x_mmsc=mscaler.transform(train_x)#正規化
mscaler.fit(train_y)#読み込み
train_y_mmsc=mscaler.transform(train_y)#正規化
#テストデータの説明変数を正規化
mscaler.fit(test_x)
test_x_mmsc=mscaler.transform(test_x)
mscaler.fit(test_y)
test_y_mmsc=mscaler.transform(test_y)

#モデルインスタンス
model=LinearRegression()
model.fit(train_x_mmsc, train_y_mmsc)#予測モデル構築
print("[決定係数(データの精度)]\n",model.score(test_x_mmsc,test_y_mmsc))#決定係数の表示(0.5(50%)以上の精度が目安)

# モデルを保存
filename = 'multiple_regression_analysis.sav'
pickle.dump(model, open(filename, 'wb'))
# 保存したモデルをロード
load_model = pickle.load(open(filename, 'rb'))

# 偏回帰係数算出
coefficie=pd.DataFrame(dataset.feature_names, columns=['colum_name'])
coefficie['coefficient'] = pd.DataFrame(load_model.coef_.T)
print("[偏回帰係数(目的変数に対する相関度)]\n",coefficie)

# 実際の住宅価格
re_test_y = mscaler.inverse_transform(test_y_mmsc)#正規化から逆変換
act_df=pd.DataFrame(re_test_y)
act_df.columns=['actual']
act_df.reset_index(drop=True, inplace=True)#indexリセット

# 学習結果からの予想住宅価格
test_x_mmsc_df=pd.DataFrame(test_x_mmsc)
test_x_predict=mscaler.inverse_transform(load_model.predict(test_x_mmsc_df))#予測値結果を正規化から逆変換
fc_df=pd.DataFrame(test_x_predict)
act_df['forecast']=fc_df #列追加
act_df.head() # 先頭5行表示


# In[ ]:




