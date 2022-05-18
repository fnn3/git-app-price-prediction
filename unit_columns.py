#!/usr/bin/env python
# coding: utf-8

# ## Uredivanje i ciscenje vrijednosti stupaca units dataframea 

# #### ucitavanje df generiranog u unit_fac nb, 240 rijesenih stupaca i 151 prazan. potrebno rijesiti iznimke i distance koji su na razini property.

# In[66]:


import pandas as pd


# ### Ucitavanje potrebnih tablica

# In[67]:


units = pd.read_csv("gen_data/units_all_fac-01.csv").drop("id_property.1", axis =1)
units.head(3)


# In[68]:


facility = pd.read_csv("gen_data/float_facility.csv",index_col="Unnamed: 0")
facility.head(3)


# In[69]:


values = pd.read_csv("gen_data/valuenum.csv",index_col="Unnamed: 0")
values.head(3)


# ### Definiranje praznih stupaca

# In[70]:


units.columns
prazni=[]
rijeseni=[]
for i in units.columns:
    if (units[i]==0).all():
        prazni.append(i)
    else:
        rijeseni.append(i)
print("prazni: ",len(prazni))
print("rijeseni: ",len(rijeseni))
print(len(prazni)+len(rijeseni))
print(len(units.columns))


# In[71]:


pr_units = units[['id_property', 'id']+prazni]
pr_units.head(3)


# In[72]:


facility[facility["facility_code"]=="air_condition"]


# ### Provjera unita koji nemaju facility i obrnuto

# In[73]:


fac_id_ls = list(facility["id_property_unit"].unique())


# In[74]:


n_unit=set(units["id"].to_list())


# In[75]:



unit_id = n_unit.intersection(fac_id_ls)
ls_unit = list(unit_id)

print(len(unit_id))
print(len(ls_unit))


# In[76]:


print(len(facility["id_property_unit"].unique()))
print(len(units["id"].to_list()))
print(len(unit_id))


# In[81]:


id_units = units.set_index(units["id"])
id_units.head()


# In[78]:


facility.shape


# In[79]:


id_fcs.loc[[3623,23113]]


# In[82]:



id_unt = id_units.loc[ls_unit]
id_unt.shape
id_unt.head()
fn_units = id_fcs["id_property_unit"].unique()
len(fn_units)


# In[83]:


id_unt.head()


# In[84]:


id_unt.shape


# In[85]:


"""id_unt.to_csv("gen_data/units_N1851-01.csv")"""


# In[113]:


fac0 = facility[facility["id_property_unit"]==0].set_index(fac0["id_property"])
fac0.head(3)
#72 000 zapisa


# In[ ]:





# In[ ]:




