#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt


# In[39]:


df = pd.read_csv("gen_data/gen2/units_df.csv")
df


# In[5]:


df_price = pd.read_csv("gen_data/gen2/Unit_cjenik.csv")
df_price


# ## Micanje pologa unita

# In[6]:


df_price.name.unique()


# In[7]:


df_price.set_index("id_unit")


# In[8]:


df_price.drop(df_price[df_price['name'] == "CM - Polog pri dolasku"].index, inplace = True)
df_price.drop(df_price[df_price['name'] == "CM - Dodatak % za kratki boravak 1 - 2 dana (po danu)"].index, inplace = True)


# In[35]:


df_price


# ### Dobivanje unita s cijenom 

# In[9]:


units = pd.Series(list(set(df["id"].tolist()) & set(df_price["id_unit"].tolist())))
units


# In[10]:


df.set_index(df["id"],inplace=True)


# In[11]:


df_full = df.loc[units]
df_full


# In[12]:


df_price.set_index(df_price["id_unit"],inplace=True)
df_price


# In[13]:


for i in df_full["id"]:
    df_full.loc[i,"amount"]=df_price.loc[i,"amount"]
df_full[["id","amount"]]


# In[14]:


ls = df_full.columns[:-1]
ls = ls.insert(3,"amount")

df_final =df_full[ls]
df_final


# In[138]:


#df_final.to_csv("gen_data/gen2/final_units2.csv",index=False)


# ### Korelacija s cijenom

# In[17]:


sns.set(rc={'figure.figsize':(25.7,10.27)})


# In[103]:


df_vals = df_final.iloc[:,3:]
corelation1 = df_vals.corr()
color = plt.get_cmap('RdYlGn')   # default color
color.set_bad('lightblue')
color.set_under(color='white')  
color.set_over(color="black")
sns.heatmap(corelation1,annot=False,cmap=color)


# In[95]:


desc= corelation.describe().dropna(axis=1)


# In[105]:


cols =desc.columns.tolist()
df_vals = df_final.loc[:,cols]
corelation = df_vals.corr()
color = plt.get_cmap('RdYlGn')   
color.set_bad('lightblue')
color.set_under(color='white')  
color.set_over(color="black")
sns.heatmap(corelation,annot=False,cmap=color,vmin = 0.1,vmax=0.9)


# In[ ]:





# In[107]:


sns.distplot(df_full["amount"])


# In[108]:


sns.displot(df_final.loc[:,["amount","area","category","floor"]],x="amount",y="area",hue="category")


# In[109]:


g = sns.PairGrid(df_final.loc[:,["amount","area","category","floor"]])
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill=True)
g.map_diag(sns.histplot, kde=True)


# ## Korelacija znacajki sa cijenom

# In[110]:


plt.xticks(rotation=90)
sns.scatterplot(data=corelation.iloc[:,0])


# In[111]:


plt.xticks(rotation=90)
sns.lineplot(data=corelation.iloc[:,:6])


# In[112]:


corelation.kitchen


# In[113]:


plt.xticks(rotation=90)
sns.lineplot(data=corelation.loc[:,["amount","kitchen"]])


# In[114]:


sns.lineplot(data=corelation.iloc[:,30:40])


# In[115]:


#sns.scatterplot(data=corelation)


# ## Podjela po beds_basic i pregled korelacija

# In[130]:


df_4bed = df_final[df_final["beds_basic"]==4]


# In[131]:


df_vals4 = df_4bed.iloc[:,3:]
corelation4bed = df_vals4.corr()
sns.heatmap(corelation4bed,annot=False)


# In[137]:


desc4= corelation4bed.describe().dropna(axis=1)
cols1 =desc4.columns.tolist()
df_vals4 = df_4bed.loc[:,cols1]
corelation4 = df_vals4.corr()
color = plt.get_cmap('RdYlGn')   
color.set_bad('lightblue')
color.set_under(color='white')  
color.set_over(color="black")
sns.heatmap(corelation4,annot=False,cmap=color,vmin = 0.05,vmax=0.9)


# In[118]:


sns.distplot(df_4bed["amount"])


# In[119]:


g = sns.PairGrid(df_4bed.loc[:,["amount","area","category","floor"]])
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill=True)
g.map_diag(sns.histplot, kde=True)


# In[120]:


plt.xticks(rotation=90)
sns.scatterplot(data=corelation4bed.iloc[:,0])


# In[121]:


sns.jointplot(data = df_4bed,x = "unit_living_equipment",y="amount",kind="reg",size=10)


# In[122]:


sns.jointplot(data = df_4bed,x = "category",y="amount",kind="reg",size=10)


# In[ ]:




