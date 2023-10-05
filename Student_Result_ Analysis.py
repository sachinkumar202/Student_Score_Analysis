#!/usr/bin/env python
# coding: utf-8

# ### Load Library

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Load Data set

# In[2]:


df = pd.read_csv("Students_Exam.csv")
print(df.head())


# In[3]:


df


# ### Data infomation

# In[4]:


df.info()


# In[5]:


df.describe()


# ### Find Null Values

# In[7]:


df.isnull().sum()


# ### Drop unnamed column

# In[8]:


df = df.drop("Unnamed: 0", axis = 1)
print(df.head())


# ### Gender Distribution

# In[24]:


plt.figure(figsize= (5,5))
ax = sns.countplot(data = df, x = "Gender")
plt.title("Gender Distribution")
ax.bar_label(ax.containers[0])
plt.show()


# ## From the above chart  we have analysed that:
# ## the Number of females in the data is more then the number of males

# In[14]:


df.columns


# In[17]:


gb = df.groupby("ParentEduc").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore": 'mean'})
print(gb)


# In[25]:


sns.heatmap(gb, annot = True)
plt.title("Relationship b/w Parents's Eductions & Student's Score")
plt.show()


# In[21]:


# from the above chart we have concluded that  the education of the parents have a good 


# In[22]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean', "ReadingScore": 'mean', "WritingScore": 'mean'})
print(gb1)


# In[28]:


sns.heatmap(gb1, annot = True)
plt.title("Relationship b/w Parents's Marital Status & Student's Score")
plt.show()


# ### from the above chart we have concluded  there no/neglible impact o the  stuent's score due to their parents marital status

# In[ ]:





# In[31]:


## Find outlier


# In[32]:


sns.boxplot(data = df , x= "MathScore")
plt.show()


# In[33]:


sns.boxplot(data = df , x= "ReadingScore")
plt.show()


# In[34]:


sns.boxplot(data = df , x= "WritingScore")
plt.show()


# In[36]:


df.columns


# In[37]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[48]:


groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()



l= ["group A","group B", "group C", "group D", "group E"]
mylist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mylist, labels= l, autopct ="%1.2f%%")
plt.title("Distribution of Etnic Groups")
plt.show()


# In[51]:


ax = sns.countplot(data = df , x = "EthnicGroup")
ax.bar_label(ax.containers[0])


# In[ ]:




