#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("gen_data/gen2/nopca_standard.csv")
df


# In[3]:


df4=df[df["beds_basic"]==4]
df4.reset_index(inplace=True,drop=True)
df4


# In[4]:


X=df4.iloc[:,4:]
Y=df4.loc[:,"amount"]


# In[5]:


X.shape


# In[6]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y)


# In[7]:


x_train.shape


# In[8]:


y_train.mean(), y_test.mean()


# In[9]:


plt.hist(y_train)


# In[ ]:





# In[65]:


import tensorflow as tf
#import keras

model_1 = tf.keras.models.Sequential()
model_1.add(tf.keras.Input(shape=(247,)))
#model_1.add(tf.keras.layers.Dense(247, activation="relu"))
model_1.add(tf.keras.layers.Dense(128, activation="relu"))
#model_1.add(tf.keras.layers.Dense(64, activation="relu"))
#model_1.add(tf.keras.layers.Dropout(0.05))
model_1.add(tf.keras.layers.Dense(1))
model_1.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.003), metrics=["mse"])
#model_1.compile(loss=config_1.loss_function, optimizer=tf.keras.optimizers.Adam(config_1.learning_rate), metrics=["accuracy"])


# In[66]:


model_1.fit(x_train, y_train, batch_size=16, epochs=300, validation_data=(x_test,y_test))


# ## app price <250

# In[68]:


df2 = df[df["amount"]<=250]
df2


# In[69]:


df24=df2[df2["beds_basic"]==4]
df24.reset_index(inplace=True,drop=True)
df24


# In[70]:


X=df24.iloc[:,4:]
Y=df24.loc[:,"amount"]


# In[75]:


x_train2, x_test2, y_train2, y_test2 = train_test_split(X, Y)
plt.hist(y_train2)


# In[81]:


y_train2.mean(), y_test2.mean(),y_train2.std(),y_test2.std()


# In[77]:


model_2 = tf.keras.models.Sequential()
model_2.add(tf.keras.Input(shape=(247,)))

model_2.add(tf.keras.layers.Dense(128, activation="relu"))

model_2.add(tf.keras.layers.Dense(1))
model_2.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.003), metrics=["mse"])


# In[78]:


model_2.fit(x_train, y_train, batch_size=16, epochs=300, validation_data=(x_test2,y_test2))


# In[82]:


predictions = model_2.predict(x_test2)


# In[89]:


df_rezultati = pd.DataFrame({'pred':predictions.reshape(-1,), 'test':y_test2})


# In[90]:


print(df_rezultati)


# In[91]:


df_rezultati['diff'] = df_rezultati['test'] - df_rezultati['pred']


# In[93]:


print(df_rezultati['diff'].mean())
print(df_rezultati['diff'].std())


# In[95]:


plt.hist(df_rezultati["diff"], bins=15)


# In[96]:


from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(predictions,y_test2,squared=False)
print(rmse/y_test2.mean()*100)


# In[217]:


df22=df2[(df2["beds_basic"]==2)&(df2["amount"]<=150)]
df22.reset_index(inplace=True,drop=True)
df22


# In[218]:


X2=df22.iloc[:,4:]
Y2=df22.loc[:,"amount"]


# In[219]:


x_train3, x_test3, y_train3, y_test3 = train_test_split(X2, Y2)
plt.hist(y_train3)


# In[226]:


model_3 = tf.keras.models.Sequential()
model_3.add(tf.keras.Input(shape=(247,)))
#model_3.add(tf.keras.layers.Dense(247, activation="relu"))
#model_3.add(tf.keras.layers.Dense(128, activation="relu"))
model_3.add(tf.keras.layers.Dense(64, activation="relu"))
#model_3.add(tf.keras.layers.Dense(32, activation="relu"))
model_3.add(tf.keras.layers.Dropout(0.1))
model_3.add(tf.keras.layers.Dense(1))
model_3.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=0.03), metrics=["mse"])


# In[227]:


model_3.fit(x_train3, y_train3, batch_size=16, epochs=300, validation_data=(x_test3,y_test3))


# In[222]:


predictions3 = model_3.predict(x_test3)


# In[223]:


df_rezultati2 = pd.DataFrame({'pred':predictions3.reshape(-1,), 'test':y_test3})
df_rezultati2['diff'] = df_rezultati2['test'] - df_rezultati2['pred']


# In[224]:


plt.hist(df_rezultati2["diff"], bins=15)


# In[225]:


from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(predictions3,y_test3,squared=False)
print(rmse/y_test3.mean()*100)

