#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import plotly as py

# In[3]:


df = pd.read_csv('AB_NYC_2019.csv')


# In[4]:


df.info()


# In[5]:


df.head(10)


# In[6]:


df['last_review'] = pd.to_datetime(df['last_review'])


# In[7]:


df['name'] = df.name.str.title()


# In[8]:


df.isnull().sum()


# In[9]:


df['host_name'].fillna(value = 'Unknown', inplace = True)


# In[10]:


df = df.drop('calculated_host_listings_count', axis = 1)


# In[11]:


df['last_review'].fillna(value = '', inplace = True)


# In[12]:


df['reviews_per_month'].fillna(value = df['reviews_per_month'].mean(), inplace = True)


# In[13]:


df['reviews_per_month'] = df['reviews_per_month'].round(3)


# In[14]:


df.head(10)


# In[15]:


duplicate_row = df[df.duplicated()]


# In[16]:


duplicate_row


# In[17]:


df


# In[28]:


df.info()


# In[25]:


df['name'].fillna(value='Unknown', inplace=True)


# In[27]:


df['last_review'].fillna(value='-', inplace=True)


# In[33]:


df.to_csv("D:\\hasil.csv", index=False)

