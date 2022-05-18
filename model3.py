#!/usr/bin/env python
# coding: utf-8

# In[15]:


import matplotlib.pyplot as plt


# In[16]:


import pandas as pd


df = pd.read_csv("gen_data/gen2/nopca_standard.csv")
df


# In[17]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X=df.loc[:,df.columns[2]].to_numpy().reshape(-1, 1)
scaler.fit(X)

scale_ar = scaler.transform(X)
scale_ar


# In[18]:


df["beds_basic"]=scale_ar
df


# In[19]:


df=df[df["amount"]<=250]
df


# In[20]:


Y=df.loc[:,"amount"]
df.drop("amount",axis=1,inplace=True)
X=df.iloc[:,2:]
X


# In[21]:


plt.hist(Y)


# In[22]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y)


# In[24]:


y_train.mean(), y_test.mean(),y_train.std(),y_test.std()


# In[26]:


import tensorflow as tf

model_2 = tf.keras.models.Sequential()
model_2.add(tf.keras.Input(shape=(248,)))
#model_2.add(tf.keras.layers.Dense(247, activation="relu"))
model_2.add(tf.keras.layers.Dense(128, activation="relu"))
#model_2.add(tf.keras.layers.Dense(64, activation="relu"))
#model_2.add(tf.keras.layers.Dropout(0.05))
model_2.add(tf.keras.layers.Dense(1))
model_2.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.003), metrics=["mse"])
#model_2.compile(loss=config_1.loss_function, optimizer=tf.keras.optimizers.Adam(config_1.learning_rate), metrics=["accuracy"])


# In[28]:


model_2.fit(x_train, y_train, batch_size=16, epochs=300, validation_data=(x_test,y_test))


# In[29]:


predictions = model_2.predict(x_test)


# In[31]:


df_rezultati = pd.DataFrame({'pred':predictions.reshape(-1,), 'test':y_test})


# In[32]:


df_rezultati


# In[33]:


df_rezultati['diff'] = df_rezultati['test'] - df_rezultati['pred']


# In[34]:


print(df_rezultati['diff'].mean())
print(df_rezultati['diff'].std())


# In[35]:


plt.hist(df_rezultati["diff"], bins=15)


# In[36]:


from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(predictions,y_test,squared=False)
print(rmse/y_test.mean()*100)

