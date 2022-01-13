#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('heart_kaggle_data.csv')


# In[3]:


data.head()


# In[66]:


data


# In[5]:


data.shape


# In[6]:


pd.DataFrame(data)


# In[13]:


data.isna().sum()


# In[65]:


(data == 0).astype(int).sum(axis=0)


# - Who is the 1 person with a restingbp of 0?
# - Why are there so many 0's for Cholesterol?
# - FastingBS was a 1 if >120 mg/dl and 0 otherwise
# - Old peak is a numeric value measured in depression. What other information is there on it?
# - HeartDisease was 1 if they have Heart Disease and 0 if they dont

# In[68]:


data.sort_values('RestingBP', ascending=True).head()


# In[71]:


data.iloc[449]


# - Entry 449 has a restingbp of 0 and 0 cholesterol. Missing Data probably

# In[11]:


data.describe


# From here forward I found the Mean, median, mode, std, range, and number of unique values foe each column where it made sense to do so

# - Mean

# In[26]:


data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']].mean()


# - Mode

# In[27]:


data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']].mode()


# - Standard Deviation

# In[28]:


data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']].std()


# - Range

# In[35]:


range_of_data = (data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']].max() - data[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']].min())


# In[36]:


print(range_of_data)


# - Number of Unique Values

# In[48]:


unique_ages = len(pd.unique(data['Age']))
unique_restingbps = len(pd.unique(data['RestingBP']))
unique_cholesterols = len(pd.unique(data['Cholesterol']))
unique_fastingbs = len(pd.unique(data['FastingBS']))
unique_maxhrs = len(pd.unique(data['MaxHR']))
unique_oldpeaks = len(pd.unique(data['Oldpeak']))
unique_heartdisease = len(pd.unique(data['HeartDisease']))


# In[50]:


print(unique_ages)
print(unique_restingbps)
print(unique_cholesterols)
print(unique_fastingbs)
print(unique_maxhrs)
print(unique_oldpeaks)
print(unique_heartdisease)


# - I need to look into what Oldpeak is and check why there are some missing values (0's) for cholesterol

# In[81]:


data[data["Cholesterol"] != 0]["Cholesterol"].mean()


# In[82]:


data[data["Cholesterol"] != 0]["Cholesterol"].mode()


# In[83]:


data[data["Cholesterol"] != 0]["Cholesterol"].median()


# In[84]:


data[data["Cholesterol"] != 0]["Cholesterol"].std()


# - I will impute missing cholesterol values with the average

# In[ ]:




