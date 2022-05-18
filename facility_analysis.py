#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib

facilities = pd.read_csv('data/property_facilities.csv', delimiter=';')
facilities.head(3)


# In[18]:


freq = facilities["facility_sub_grp"].value_counts()
freq.head(50)
freq.to_csv("gen_data/sub_grp_frequency.csv")


freq0 = freq[0:40]
freq1 = freq[40:]
freq.head(5)


# In[10]:


freq0.plot.bar()


# In[11]:


freq1.plot.bar()


# In[13]:


uniq_fac = pd.read_csv('gen_data/facilities.csv', delimiter=';')
uniq_fac.head()


# In[14]:


uniq_fac.shape


# In[15]:


in_vector = pd.read_csv('data/input_fac.csv', delimiter=';')["facility_inputs"].tolist()


ls=[]
lsprazni=[]
for index,i in enumerate(facilities['facility_code']):
    if i not in in_vector:
        ls.append(index)
print(len(ls))


facilities = facilities.drop(ls)

print(facilities.shape)
print(facilities.head())


# In[16]:


freq2 = facilities["facility_code"].value_counts()
freq2.head(5)


# In[17]:


freq2.plot.bar()

