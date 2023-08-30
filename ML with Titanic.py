#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


dtf= pd.read_csv('train.csv')


# In[7]:


dtf.head()


# In[8]:


dtf.describe()


# In[9]:


dtf.isnull().sum()


# In[10]:


# missing vlaue remove 
df_use= dtf.copy()
df_use= df_use.dropna()
df_use.info()


# In[24]:


# imputation of data for missing value i.e. replacing data 
df_u1= df_use.copy()
    df_u1['Age']= df_u1['Age'].fillna(df_u1['Age'].mean()) # replacing with the mean value 
    df_u1['Cabin']= df_u1['Cabin'].fillna(df_u1['Cabin'].value_counts().index[0]) # repalcing with majority count of the class
    df_u1['Embarked']= df_u1['Embarked'].fillna(df_u1['Embarked'].value_counts().index[0])
df_u1.head()


# In[16]:


import seaborn as sns


# In[15]:


sns.countplot(x= 'Survived', data= df_u1)


# In[17]:


df_u1['Survived'].value_counts()


# In[18]:


sns.boxplot(data=dtf, x='Pclass', y='Age')


# In[21]:


sns.barplot(data= dtf, x= 'Pclass', y= "Fare")


# In[23]:


sns.boxplot(data=dtf, x="Pclass", y='Age')


# In[41]:


dtf_cabin= dtf[['Cabin', 'Fare']]
dtf_cabin= dtf_cabin.dropna()
dtf_cabin["Cabin"].unique()


# In[46]:


def clean_cabin(cabin):
    return(cabin[0])dtf_cabin = dtf_cabin['Cabin'].apply(clean_cabin)


# In[47]:


sns.catplot(data=dtf_cabin, x= 'Cabin', y= 'Fare')


# In[49]:


sns.barplot(data= dtf, x='Survived', y= 'Fare')


# In[51]:


sns.barplot(data=dtf, x='Pclass', y='Survived')


# In[ ]:




