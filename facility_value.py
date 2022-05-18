#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


facility = pd.read_csv("gen_data/facility_grp.csv")
facility.head(3)


# ### Dobivanje jedinstvenih vrijednosti znacajki bez brojcanih vrijednosti

# In[4]:


values = facility["value"].unique()
val=[]
for i in values:
    try:
        int(i[-1]) or int(i[0])
    except:
        val.append(i)

val = pd.Series(val)
print(val)


# ### Definiranje funkcije za sortiranje vrijednosti znacajki ovisno o nazivu vrijednosti

# In[5]:


def sort(string,val):
    mask = val.str.contains(string)
    dl=[]
    for index,i in enumerate(val):
        if mask[index] == False:
            dl.append(index)
    value = val.drop(labels=dl)
    return value




# In[6]:


sort("yes",val)


# In[7]:


val_column = val.tolist()
#print(val_column)
clean_values =[0] * len(val_column)
print(len(clean_values),len(val_column))


# In[8]:


""" dict = {"values":val_column,"clean":clean_values}

values_df = pd.DataFrame.from_dict(dict)
values_df = values_df.set_index(values_df["values"])
values_df = values_df.drop(["values"],axis = 1)
values_df.head() """


values_s = pd.Series(clean_values,index=val_column)
values_s.head()


# In[9]:


values_s["on"] = 1
values_s["off"] = -1
print(values_s["off"])


# In[10]:


ls = sort("price",val).tolist()
ls.remove(ls[3])
print(ls)


# In[11]:


for i in ls:
    values_s[i]=1
    #print(values_s[i])
values_s["yes-electicity-in-price"]


# In[12]:


ls1 = sort("no",val).tolist()
ls1.remove(ls1[6])
ls1.remove(ls1[-2])
print(ls1)
values_s['pets_free_no_charges']=1
#micanje pets free no charges i nan i postavljanje pets free na values_s =1


# In[13]:


for i in ls1:
    values_s[i]=-1
    #print(values_s[i])

    
values_s["no-gas"]


# In[14]:


ls2 = sort("yes",val).tolist()
ls2.remove(ls2[4])
print(ls2)

for i in ls2:
    values_s[i]=1
    #print(values_s[i])

    
values_s["yes-free"]


# In[15]:


ls3 = sort("price",val).tolist()
#ls3.remove(ls3[4])
print(ls3)

values_s['deposit-is-obligatory'] = -1
values_s['yes_obligatory'] = -1
values_s['towels_change_daily']=3
values_s['towels_change_weekly','pets_charges_may_apply'] = 2
values_s[["not_needed",'towels_pperson_standard_plus_mini','towels_pperson_set','towels_pperson_2mini','towels_pperson_standard','final-cleaning-in-price','pets_upon_request']] = 1
print(values_s['towels_pperson_standard'])
print(values_s['towels_pperson_set'])

""" for i in ls2:
    values_s[i]=1
    #print(values_s[i])

    
values_s["yes-free"] """


# In[16]:


ls4 = sort("park",val).tolist()
#ls4.remove(ls4[4])
print(ls4)
values_s['park_private', 'park_loc_on_site', 'parking_yes_free']=2
values_s[ 'park_public', 'park_loc_off_site', 'parking_yes_paid']=1
print(values_s['park_private'])


# In[17]:


ls5 = sort("int",val).tolist()
#ls5.remove(ls5[4])
print(ls5)
values_s[ 'int-con-all-rooms', 'int-con-entire-property']=2
values_s['int-con-public-areas', 'int-con-business-centre', 'int-con-some-rooms',"wifi"]=1
print(values_s["wifi"])


# In[18]:


ls6 = sort("floor",val).tolist()
#ls6.remove(ls6[4])
print(ls6)
values_s['final-cleaning-in-price']=1
values_s['final-cleaning-charged']=-1
values_s[ 'ground_floor',"entire_property", 'upper_floor_reachable_by_stairs_only'] = 1
values_s['entire_property_on_ground_floor'] = 6
values_s['first_floor'] = 2
values_s['second_floor'] = 3
values_s['third_floor'] = 4
values_s['fourth_floor'] = 5


# In[19]:


ls7 = sort("floor",val).tolist()
#ls6.remove(ls6[4])
print(ls7)
values_s['extra_beds_available','bed_linen_change_weekly'] = 1


# In[20]:


v_index =values_s.index
values_s


# In[37]:


facility[facility["value"]=="on"]["value"]


# In[ ]:





# In[22]:


valuenum = values_s[values_s!=0]
valuenum.to_csv("gen_data/valuenum.csv")


# In[23]:


valuenum.index


# In[24]:


facility_v = facility.replace(valuenum.index,valuenum)
#facility_v.head(50)
facility["new_values"]=facility_v["value"]


# In[ ]:





# In[25]:


facility.to_csv("gen_data/facility_nvls.csv")


# In[26]:


facilities = facility.set_index(facility["id_property_unit"])[["facility_sub_grp","facility_code", "value","new_values"]]
facilities.head()

#facilities.loc[24477]
facilities.loc[23113]


# ## uredivanje distance value u float i spremanje

# In[27]:


"""cfacility = facility.drop(facility.index[facility['new_values'] == facility["value"]])
print(facility.shape)
print(cfacility.shape)"""
                                        #krivo, brise sve distance


# In[28]:


# gornja celija brise i sve distance jer oni nemaju new value 
#cfacility.to_csv("gen_data/facility_new_only.csv")


# In[ ]:





# In[39]:


numfacility = facility

numfacility["new_values"] = pd.to_numeric(numfacility["new_values"],errors="coerce")
#print(numfacility.dtypes)
numfacility[numfacility["facility_sub_grp"]=="disg_common"]


# ### Zadrzavanje samo brojcanih vrijednosti i spremanje float_facility.csv

# In[30]:


nfacility = numfacility.dropna(subset=["new_values"])
print(nfacility.shape)
print(numfacility.shape)


# In[31]:


nfacility.to_csv("gen_data/float_facility.csv")


# In[32]:


ls8 = sort("disg",facility["facility_sub_grp"]).unique().tolist()
print(ls8)
ls9=[]
dist_grp = ['disg_common', 'disg_transport', 'disg_sea', 'disg_beaches', 'disg_shops', 'disg_services', 'disg_public_parking']
for i in dist_grp:
    lsi = facility[facility["facility_sub_grp"]==i]["facility_code"].unique().tolist()
    for j in lsi:
        ls9.append(j)
print(ls9)

dst =facility[facility["facility_sub_grp"]=="disg_common"]["id_property_unit"].unique()
print(dst)


# In[43]:


facility[facility["facility_sub_grp"]=="disg_transport"]


# ## Grupiranje znacajki prema facility_sub_grp

# In[44]:


facilities["facility_sub_grp"].unique()


# In[35]:


facilities[facilities["facility_sub_grp"] == 'kitchen']["facility_code"].unique()


# In[36]:


facilities[facilities["facility_sub_grp"] == 'kitchen']


# In[ ]:





# In[ ]:




