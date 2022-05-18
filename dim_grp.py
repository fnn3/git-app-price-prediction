#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# In[2]:


df = pd.read_csv("gen_data/rijeseni-249.csv").drop("id.1",axis =1)
df=df.loc[:, (df != 0).any(axis=0)]
df.head(3)


# In[3]:


grps = pd.read_csv("gen_data/facility_togrp.csv").drop("Unnamed: 0",axis=1)
grps.head(3)


# In[4]:


#iz grps je potrebno izbaciti sve kodove koji nisu u df
fcodes = df.columns[7:]

no_grp=[]
grp_df = pd.DataFrame(columns = ["facility_sub_grp", "facility_code"])
for index,i in enumerate(fcodes):
    try:
        grp_df.loc[index] = [grps[grps["facility_code"]==i]["facility_sub_grp"].dropna().unique().tolist()[0],i]
    except:
        no_grp.append(i)
    
grp_df.shape


# In[5]:


grp_df.head()


# ## Potrebno na dijelu napravit PCA a dio bez grupa grupirat ili zadrzat - 
# ## spremljeno u no_grp

# In[6]:


grps[grps["facility_code"]=="sattv"]


# In[7]:


grp_df
#no_grp


# In[8]:


grps[grps["facility_sub_grp"]=="backyard"]["facility_code"].tolist()


# In[9]:


grp_list = grp_df["facility_sub_grp"].unique()


# In[10]:


# 2- category 3-area 4 - floor i 6-beds additional potrebno skalirat kao ostale features
new_df = df.loc[:,df.columns[0:6]]
new_df


# In[11]:


#scikit learn.decomposition
df.columns[7:]


# In[12]:


"""def PCA(ls):
    pass"""


# In[13]:


scaler = StandardScaler()
X=df.loc[:,df.columns[6:]]
scaler.fit(X)

scale_ar = scaler.transform(X)
len(df.columns)
#len(scale_df[0])


# In[14]:


scale_ar


# In[15]:





# In[16]:


"""codes = grp_df[grp_df["facility_sub_grp"]=="backyard"]["facility_code"].tolist()
val = df[codes].values
pca = PCA(n_components=)
"""


# In[17]:


len(grp_list)


# In[18]:


exception=[]
for i in grp_list:
    codes = grp_df[grp_df["facility_sub_grp"]==i]["facility_code"].tolist()
    n_comp = len(codes)
    pca = PCA(n_components=1)
    pca.fit(df[codes].values)
    new_df[i] = pca.transform(df[codes])
 
""" try:
        #new_df[i]= PCA(df[codes])
        pca = PCA()
        pca.fit(df[codes])
        new_df[i] = pca.transform(df[codes])
    except:
        exception.append(i)"""


# In[19]:


new_df.head()


# In[20]:


exception


# In[21]:


new_df.head(30)


# In[23]:


df_s = pd.DataFrame(scale_ar,columns=df.columns[6:])
df_s
df_all = pd.concat([new_df,df_s[no_grp]],axis=1)
df_all


# In[24]:


df_all.columns


# In[25]:


#df_all.to_csv("gen_data/PCA_nogrps_122.csv")


# In[26]:


df_all.describe()


# In[28]:




