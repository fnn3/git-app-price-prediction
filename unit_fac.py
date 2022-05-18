#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


units = pd.read_csv("gen_data/units.csv")
#units= units.set_index(units["id"])
units.head()


# In[4]:


facility_df = pd.read_csv("gen_data/float_facility.csv",index_col="Unnamed: 0")
facility_df.head()


# In[5]:


values = pd.read_csv("gen_data/valuenum.csv",index_col="Unnamed: 0")
values.head()


# In[6]:


fcode = facility_df["facility_code"].unique()
print(len(fcode))
fcode


# In[7]:


units.shape


# In[8]:


for i in fcode:
    units[i] = pd.Series([0 for x in range(len(units.index))])


# In[9]:


units.head(10)


# In[10]:


i_units =units.set_index(units["id"])
i_units.head()


# In[11]:


unbed = units[["id","twin_bed"]].set_index(units["id"])["twin_bed"]
unbed.head()


# In[12]:


unbed[25727]


# In[13]:


#lista unit id-a koji sadrze odredeni facility_code (twin_bed)

facility_df[facility_df["facility_code"]=="twin_bed"]["id_property_unit"].tolist()

# koristi se kao index za unbed series kako bi se postavio value
#unbed[facility_df[facility_df["facility_code"]=="twin_bed"]["id_property_unit"].tolist()]


# ### povlacenje vrijednosti iz facility df i spremanje brojcanih vrijednosti u units df stupce prema facility_code

# In[14]:


# vraca value kao broj za odredeni facility_code twin_bed, value = on, num_value = 1

values.loc[facility_df[facility_df["facility_code"]=="twin_bed"]["value"].unique()[0]][0]


# In[15]:


unbed[facility_df[facility_df["facility_code"]=="twin_bed"]["id_property_unit"].tolist()] = values.loc[facility_df[facility_df["facility_code"]=="twin_bed"]["value"].unique()[0]][0]


# In[16]:


unbed.head()


# In[17]:


facility_df[facility_df["facility_code"]=="twin_bed"]["id_property_unit"].tolist()


# In[ ]:





# ### Odvajanje facilitya koji su identificirani sa id_property_unit i id_property, facility na razini smj. jedinice i na razini objekta

# In[18]:


# facility koji su id na razini objekta
property_f = facility_df[facility_df["id_property_unit"]==0]["facility_code"].unique()
#property_f


# In[19]:


#facility koji su id na razini unita
unit_f = facility_df[facility_df["id_property_unit"]!=0]["facility_code"].unique()
unit_f


# In[20]:


print(len(unit_f)+len(property_f))
print(len(property_f))
print(len(fcode))


# In[21]:


# dobivanje facilitya koji imaju id unit i property, brisu se iz unit liste
#ako se pokrene dva puta celija print ostane prazan set

prop_f_set = set(property_f)
presjek = prop_f_set.intersection(unit_f)
print(presjek)
for i in presjek:
    index=np.where(unit_f==i)
    unit_f=np.delete(unit_f,index)


# In[22]:


print(len(unit_f)+len(property_f))
print(len(fcode))
print(len(unit_f))
print(len(property_f))


# In[23]:


facility_df[facility_df["facility_code"]== 'outside_area_completely_enclosed']


# ## dodavanje vrijednosti stupcima f_code u df units

# In[24]:


for i in unit_f:
    i_units[i][facility_df[facility_df["facility_code"]==i]["id_property_unit"].tolist()] = values.loc[facility_df[facility_df["facility_code"]==i]["value"].unique()[0]][0]


# In[25]:


i_units["twin_bed"]


unbed[facility_df[facility_df["facility_code"]=="twin_bed"]["id_property_unit"].tolist()] = values.loc[facility_df[facility_df["facility_code"]=="twin_bed"]["value"].unique()[0]][0]


# In[26]:


i_units.head()


# In[27]:


i_units.to_csv("gen_data/units_unitfacilities01.csv")


# ### Prijenos property facility u units df

# In[28]:


p_units = i_units.set_index(i_units["id_property"])
p_units.head()


# In[29]:


facility_df[facility_df["facility_code"]=="terrace"]["id_property"].unique().tolist()


# In[30]:


p_units.loc[1817]
p_units['terrace'].loc[facility_df[facility_df["facility_code"]=='terrace']["id_property"].tolist()]


# In[31]:


ls=[]
for i in property_f:
    try:
        p_units[i].loc[facility_df[facility_df["facility_code"]==i]["id_property"].tolist()] = values.loc[facility_df[facility_df["facility_code"]==i]["value"].unique()[0]][0]
    except:
        ls.append(i)


# In[32]:


values.loc[facility_df[facility_df["facility_code"]=="terrace"]["value"].unique()[0]][0]


# In[33]:


#len ls iz funkcije except jednaka je len praznih stupaca 
print(len(ls))


# In[34]:


# ne lovi podatke za air_condition-provjerit ostale-parties_allowed,kids_allowed
# unit_floor ima br samo 0 ili 3
# nisu azurirani distance u csv-u
"""p_units.to_csv("gen_data/units_all_fac-01.csv")"""


# In[35]:


p_units.head(20)


# In[ ]:





# In[36]:


# ne postoji u tablici units
#p_units.loc[10227]


# In[37]:


#facility_df[facility_df["id_property"]== 10227]


# In[38]:


facility_df[facility_df["facility_code"]== 'air_condition']


# ### Provjera rijesenih i praznih stupaca

# In[39]:


p_units.columns
prazni=[]
rijeseni=[]
for i in p_units.columns:
    if (p_units[i]==0).all():
        prazni.append(i)
    else:
        rijeseni.append(i)
print("prazni: ",len(prazni))
print("rijeseni: ",len(rijeseni))
print(len(prazni)+len(rijeseni))
print(len(p_units.columns))


# In[41]:


print(prazni)
with open('gen_data/prazni_stupci_ls.txt', 'w') as f:
    for item in prazni:
        f.write("%s\n" % item)

