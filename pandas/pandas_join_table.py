#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston        
import pandas as pd     

boston = load_boston() # データセットの読み込み      
df = pd.DataFrame(boston.data,columns=boston.feature_names)     
df["test_data"] = "test_data_val"       
df.loc[df.NOX < 0.5, "NOX"]=None # NaN値作成のため更新      

df2 = df.copy() # コピーテーブル作成       
df2["test_data"] = "no_join_test_data"      

df.loc[df.index[[0,1]], "test_data"]="join_key" # 1,2行目をjoinkey作成     
df2.loc[df.index[[0]], "test_data"]="join_key" # 1行目をjoinkey作成            

# 以下Ptyhon内のコードを記載し、実行


# In[2]:


df_mg=pd.merge(df,df2, how="inner", on = "test_data")
df_mg[["RM_x","AGE_x"]]


# In[3]:


df_mg=pd.merge(df,df2, how="outer", on = "test_data")
df_mg[["RM_x","AGE_x"]]


# In[ ]:




