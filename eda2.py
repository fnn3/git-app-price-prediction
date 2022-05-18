#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


df = pd.read_csv("gen_data/gen2/units_df.csv")
df.head()


# ## Analiza korelacija

# In[14]:


df_vals = df.iloc[:,3:]
corelation = df_vals.corr()
sns.heatmap(corelation,annot=False)


# In[50]:


corlist = []
column_cor = corelation.columns
for i in range(119):
    for j in range(119):
        if i!=j:
            if corelation.iloc[i,j]>=0.98:

                corlist.append(column_cor[i])
                corlist.append(column_cor[j])
print(set(corlist))
un_list = list(set(corlist))


# In[51]:


df_test = df.loc[:,un_list]
corelation2 = df_test.corr()
sns.heatmap(corelation2,annot=True)


# In[91]:


def dfs_corelation(cor_matrix, cor_score,minmax= 1):
    column_cor = cor_matrix.columns
    ls1=[]
    ls2=[]
    ls3=[]
    for i in range(119):
        for j in range(119):
            if (i!=j) & (i<j):
                if minmax ==1:
                    if corelation.iloc[i,j]>=cor_score:

                        ls1.append(column_cor[i])
                        ls2.append(column_cor[j])
                        ls3.append(corelation.iloc[i,j])
                else:
                    if corelation.iloc[i,j]<=cor_score:

                        ls1.append(column_cor[i])
                        ls2.append(column_cor[j])
                        ls3.append(corelation.iloc[i,j])

    cors = pd.DataFrame({"fac01":ls1,"fac02":ls2,"cor":ls3})
         
    return cors


# In[94]:


# arg minmax 1 za vece, 0 za manje
dfs_corelation(corelation,-0.99,0)


# In[100]:


sns.set(rc={'figure.figsize':(15.7,8.27)})
sns.boxplot(data=df.iloc[:,3:30])


# In[116]:


sns.displot(df.loc[:,["area","category","floor"]],x="floor",hue="category")


# In[117]:


g = sns.PairGrid(df.iloc[:,3:10])
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill=True)
g.map_diag(sns.histplot, kde=True)

