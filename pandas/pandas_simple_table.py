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


# In[7]:


df[["RM", "AGE"]]


# In[8]:


df.rename(columns={"RM":"af_rm", "AGE":"af_age"}, inplace=True)
df
df.rename(columns={"af_rm":"RM", "af_age":"AGE"}, inplace=True)


# In[9]:


df["flg"] = "1"
df


# In[10]:


df[df["RM"] > 6]


# In[11]:


df[["RM", "AGE"]].query('RM > 6 and AGE == "100"')


# In[12]:


df[df["NOX"].isnull()]


# In[13]:


df[df["NOX"].notnull()]


# In[14]:


df[["RM", "AGE"]].query('RM >= 6 and RM <= 8')


# In[15]:


df[df["test_data"].str.startswith('te')]


# In[16]:


df[df["test_data"].str.contains('[ぁ-んァ-ン一-龥a-z]t_d[ぁ-んァ-ン一-龥a-z]', regex=True)]


# In[17]:


df[df["test_data"].str.endswith('al')]


# In[18]:


df.loc[df.NOX < 0.5, "NOX"]=None
df


# In[19]:


df.RM.describe()


# In[20]:


df.drop(df.index[[0,2,4]],inplace=True)
df


# In[21]:


df.groupby("ZN").ZN.count()


# In[22]:


df["RM"].sort_values(ascending=True)


# In[23]:


df["RM"].sort_values(ascending=False)


# In[24]:


del df["ZN"]
df


# In[33]:


print(len(df["CHAS"]))
print(len(df.drop_duplicates(["CHAS"])))
df.drop_duplicates(["CHAS"]).head()


# In[ ]:




