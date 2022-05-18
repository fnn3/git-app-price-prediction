#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


units = pd.read_csv("gen_data/units_N1851-01.csv",encoding='utf8').drop(["id.1"],axis=1)
units = units.set_index(units["id_property"])
units.head(3)


# In[3]:


facility = pd.read_csv("gen_data/facility_nvls.csv").drop(["Unnamed: 0"], axis=1)
facility = facility.set_index(facility["id_property"])
facility.head()


# In[4]:


grps = facility["facility_sub_grp"]
grps


# In[5]:


stupci = []
infile = open('gen_data/prazni_stupci_ls.txt','r')
for line in infile:
    stupci.append(line.strip())
stupci


# In[6]:


"""ls=[]
for i in stupci:
    try:
        units[i].loc[facility[facility["facility_code"]==i]["id_property"].tolist()] = 
    except:
        ls.append(i)"""


# In[7]:


facility[facility["facility_code"]=="air_condition"]["id_property"]


# In[8]:


"""for i in stupci:
    stupac = units[i]
    for pr in units["id_property"]:
        facility[facility["id_property"]==pr]"""

    
    


# In[9]:


units= units.set_index(units["id_property"])
units.head(3)


# In[10]:


units["air_condition"]


# In[11]:


facility[(facility["id_property"]==1817) & (facility["id_property_unit"]==0) & (facility["facility_code"]=="tennis")].dropna(subset = ["facility_sub_grp","new_values"])


# In[55]:





# In[45]:


facility= facility.set_index(facility["id_property"])
facility.head(3)


# In[47]:


facility.loc[((facility["id_property"]==1817) & (facility["facility_code"]=="tennis")),"new_values"][1817]


# In[13]:


units.loc[1817]

for i in units.loc[10043]["id"]:
    print(i)


# In[14]:


units[units["id"]==3623]


# In[15]:


units = units.set_index(units["id"])
units.head(3)


# In[48]:


solounit = []
ls=[]

for pr in units["id_property"].unique():
    try:
        for unit in units[units["id_property"]==pr]["id"]:
            try:
                for stupac in stupci:
                    if float(facility[(facility["id_property"]==pr) & (facility["facility_code"]==stupac)]["new_values"][pr]) != 0:
                        units.loc[unit,stupac] = float(facility.loc[(facility["id_property"]==pr) & (facility["facility_code"]==stupac),["new_values"]][pr])
            except:
                solounit.append(stupac)
    except:
        print(pr)


# In[52]:


len(solounit)


# In[50]:


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


# In[61]:


units[["id","id_property", "category", "area", "floor", "beds_basic" ,"beds_additional",'internet-paidorfree', 'internet-connectiontype', 'internet-location']].head(3)


# In[ ]:





# In[19]:


stupci_set = set(stupci)
presj = stupci_set.intersection(prazni)
print(presj)


# In[20]:


print(rijeseni)


# In[21]:


for pr in units["id_property"].unique():
    print(pr)


# In[22]:


units[units["id_property"]==10043]


# In[23]:


#units.to_csv("gen_data/rijeseni-249.csv")


# In[24]:


full_units = units.drop(prazni,axis=1)
full_units.shape


# In[25]:


stats = full_units.describe()
#stats.to_csv("gen_data/stat.csv")


# In[26]:


full_units.head(3)


# In[27]:


facility = facility.set_index(facility["id_property_unit"])


# In[68]:


desc = full_units.describe()
desc


# In[69]:





# In[29]:


full_columns = full_units.columns


# In[70]:



  


# In[31]:


sub_grp = facility[["facility_sub_grp","facility_code"]]
sub_grp.reset_index(inplace=True)
sub_grp.head()
fgrp = sub_grp["facility_sub_grp"].unique()
fgrp
fcodes = sub_grp["facility_code"].unique()
#print(fcodes)
facility[facility["facility_sub_grp"]=="kitchen"]["facility_code"].unique()


# In[ ]:





# In[32]:


""" df = pd.DataFrame(columns=['lib', 'qty1', 'qty2'])
for i in range(5):
    df.loc[i] = ['name' + str(i)] + list(randint(10, size=2))"""


no_grp=[]
grp_df = pd.DataFrame(columns = ["facility_sub_grp", "facility_code"])
for index,i in enumerate(fcodes):
    try:
        grp_df.loc[index] = [facility[facility["facility_code"]==i]["facility_sub_grp"].dropna().unique().tolist()[0],i]
    except:
        no_grp.append(i)
    
grp_df.shape


# In[33]:


grp_df.head(50)


# In[34]:


#grp_df.to_csv("gen_data/facility_togrp.csv")


# In[35]:


#78 grupa
grp_df["facility_sub_grp"].unique()


# In[36]:


units.head()


# In[37]:


units_grp = units[["id","id_property", "category", "area", "floor", "beds_basic" ,"beds_additional"]]
units_grp


# In[ ]:




