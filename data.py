#!/usr/bin/env python
# coding: utf-8

# ## Ucitavanje df smjestaja-unita

# In[2]:


import numpy as np
import pandas as pd

p_unit = pd.read_csv('data/property_unit.csv', delimiter=';')
#p_unit.head(3)


# ## Ucitavanje df znacajki-facilities

# In[11]:


facilities = pd.read_csv('data/property_facilities.csv', delimiter=';')
facilities.head(3)


# ## Dobivanje podataka o znacajkama i grupama znacajki

# In[4]:


uniq_facilities = pd.read_csv('gen_data/facilities.csv', delimiter=';')
uniq_facilities.head(3)


# In[5]:


mask = uniq_facilities['0'].str.contains("pool")
mask.head()
for index,i in enumerate(mask):
    if i == True:
        print(uniq_facilities["0"][index])


# In[6]:


mask1 = facilities['facility_sub_grp'].str.contains("kitchen")
mask.head()
sr = []
for index,i in enumerate(mask1):
    if i == True:
        sr.append(facilities["facility_code"][index])
        #print(facilities["facility_code"][index])

def unique(list1):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

unique_ls = unique(sr)

print(unique_ls)


# ## units-Postavljanje id unita kao id dataframe i drop stupaca
# 

# In[7]:


p_unit = p_unit.set_index(p_unit["id"])
p_unit = p_unit.drop(["id"],axis=1)
p_unit.head()


# In[8]:


p_unit.columns

units = p_unit[["id_property", "category", "area", "floor", "beds_basic", "beds_additional"]]
units.to_csv("gen_data/units.csv")

    


# In[9]:


units.head()


# ### facilities - Postavljanje id unita kao id u df znacajki i ciscenje stupaca 

# In[12]:


facilities = facilities.set_index(facilities["id_property_unit"])[["id_property","facility_sub_grp","facility_code", "value"]]
facilities.head()


# In[ ]:


facilities.to_csv("gen_data/facility_grp.csv")


# ### indeksiranje znacajki pojedinog unita

# In[ ]:


facilities.loc[23113]


# ### Podaci o grupama i vrijednostima znacajki

# In[ ]:


groups = facilities["facility_sub_grp"].unique()
groups


# In[ ]:


values = facilities["value"].unique()
val=[]
for i in values:
    try:
        int(i[-1]) or int(i[0])
    except:
        val.append(i)

val = pd.Series(val)
print(val)

len(val)


# In[ ]:


mask = val.str.contains("no")
mask.head()
dl=[]
for index,i in enumerate(val):
    if mask[index] == False:
        dl.append(index)
value = val.drop(labels=dl)
#drop pets free no charge i postavit vrijednosti na 0 ili -1
#value = value.drop([86])
print(value)


# In[ ]:




