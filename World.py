#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")  #using style ggplot

get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt


# In[2]:


df=pd.read_csv("WorldHappiness_Corruption_2015_2020.csv")

# shows the first 5 rows of dataset
df.head()


# In[3]:


# Shape of the Dataset

print("The Shape DataSet = {} ".format(df.shape))


# In[4]:


# Lokking for the null values in the dataset

df.isnull().sum()


# In[5]:


# Descriptive stats of the dataset
df.describe().round(2)


# In[6]:


# Creating the function for the line plot 
def line_plot_year():
    """This function will display the average happines indexes for the each continent .
    From 2015-2020.
    """
    
    piv_avg=df.pivot_table(index="continent",columns="Year",values="happiness_score")
    piv_avg.round(2)
    return piv_avg.plot(figsize=(15,10))
line_plot_year()


# In[7]:


# All continent don't has more different in happiness in 5 years but the North America in 2016 had increase score but then in decreasing


# 

# In[8]:


labels = df["Year"].value_counts().index
sizes = df["Year"].value_counts()
plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, rotatelabels=False, autopct='%1.1f%%')
plt.title('YEAR',color = 'purple',fontsize = 15)
plt.show()


# In[9]:


#Histogram of the Happiness score 
plt.figure(figsize=(9,6))
plt.hist(data=df, x='happiness_score')
plt.title('Distribution of Happiness Score (All Years)')


# In[ ]:




