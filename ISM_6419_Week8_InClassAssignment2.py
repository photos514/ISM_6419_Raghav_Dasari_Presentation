#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = "C:\\Users\\rdasari\\Desktop\\COVID-19\\04-02-2020.csv"
df = pd.read_csv(data)
df.head()


# In[5]:


df1 = pd.DataFrame()
df1['Combined_Key'] = df['Combined_Key']
df1['Deaths'] = df['Deaths']
df1.set_index('Combined_Key',drop=True,inplace=True)
df1.head()


# In[9]:


df1.groupby(['Combined_Key']).sum().sort_values("Deaths",ascending=False)[:20].plot.bar(color = 'blue')
plt.xlabel('Combined_Key') 
plt.ylabel('Deaths')
plt.title('Top 20 Countries/Cities by Number of Deaths as on 04-02-2020')
plt.show()


# In[10]:


df2 = pd.DataFrame()
df2['Combined_Key'] = df['Combined_Key']
df2['Confirmed'] = df['Confirmed']
df2.set_index('Combined_Key',drop=True,inplace=True)
df2.head()


# In[13]:


df2.groupby(['Combined_Key']).sum().sort_values("Confirmed",ascending=False)[:10].plot.bar(color = 'red')
plt.xlabel('Combined_Key') 
plt.ylabel('Confirmed')
plt.title('Top 10 Countries/Cities by Number of Confirmed Cases as on 04-02-2020')
plt.show()


# In[14]:


df2 = pd.DataFrame()
df2['Combined_Key'] = df['Combined_Key']
df2['Recovered'] = df['Recovered']
df2.set_index('Combined_Key',drop=True,inplace=True)
df2.head()


# In[15]:


df2.groupby(['Combined_Key']).sum().sort_values("Recovered",ascending=False)[:10].plot.bar(color = 'green')
plt.xlabel('Combined_Key') 
plt.ylabel('Recovered')
plt.title('Top 10 Countries/Cities by Number of Recovered Cases as on 04-02-2020')
plt.show()


# In[ ]:




