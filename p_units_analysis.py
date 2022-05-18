#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[35]:


df = pd.read_csv('data/property_facilities.csv', delimiter=';')
df.set_index(df["id_property_unit"],inplace=True)
df


# In[36]:


df_fin= pd.read_csv("gen_data/gen2/final_units.csv")
df_fin.set_index(df_fin.id,inplace=True)
df_fin


# In[37]:


units = pd.read_csv("gen_data/gen2/unit_cjenik.csv")
units.set_index(units.id_unit,inplace=True)
units


# In[38]:


units.name.unique()


# ### Prije slanja tablice izbacit Polog pri dolasku

# In[39]:


#units.drop(units[units["name"]=='CM - Polog pri dolasku']["id_unit"],axis=0)


# In[55]:


ls=df_fin.id.tolist()


# In[56]:


df_active = df.loc[ls,:]
df_active


# In[59]:


len(df_active.id_property_unit.unique())


# In[ ]:


#veca frekvencija od broja aktivnih unita


# In[60]:


"""freq = df_active["facility_code"].value_counts()
freq"""


# In[63]:


df_active[(df_active.facility_code=="dishes") & (df_active.object=="property_unit")]


# In[66]:


df_act_unit = df_active[df_active.object=="property_unit"]


# In[51]:


sns.set(rc={'figure.figsize':(23.7,7.27)})


# In[68]:


freq = df_act_unit["facility_code"].value_counts()
freq
freq.plot.line()


# In[77]:


freq.plot.bar()

