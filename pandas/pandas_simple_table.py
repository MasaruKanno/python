#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn.datasets import load_boston        
import pandas as pd     

boston = load_boston() # データセットの読み込み      
df = pd.DataFrame(boston.data,columns=boston.feature_names)
df["test_data"] = "test_data_val"       
df.loc[df.NOX < 0.5, "NOX"]=None # NaN値作成のため更新
# 以下Ptyhon内のコードを記載し、実行
df


# In[2]:


df[["RM", "AGE"]]


# In[3]:


df.rename(columns={"RM":"af_rm", "AGE":"af_age"}, inplace=True)
df


# In[4]:


df["flg"] = "1"
df


# In[7]:


df[df["RM"] > 6]


# In[8]:


df[["RM", "AGE"]].query('RM > 6 and AGE == "100"')


# In[9]:


df[df["NOX"].isnull()]


# In[10]:


df[df["NOX"].notnull()]


# In[11]:


df[["RM", "AGE"]].query('RM >= 6 and RM <= 8')


# In[12]:


df[df["test_data"].str.startswith('te')]


# In[13]:


df[df["test_data"].str.contains('[ぁ-んァ-ン一-龥a-z]t_d[ぁ-んァ-ン一-龥a-z]', regex=True)]


# In[14]:


df[df["test_data"].str.endswith('al')]


# In[15]:


df.loc[df.NOX < 0.5, "NOX"]=None
df


# In[16]:


df.RM.describe()


# In[17]:


df.drop(df.index[[0,2,4]],inplace=True)
df


# In[18]:


df.groupby("ZN").ZN.count()


# In[19]:


df["RM"].sort_values(ascending=True)


# In[20]:


df["RM"].sort_values(ascending=False)


# In[ ]:




