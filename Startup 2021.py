#!/usr/bin/env python
# coding: utf-8

# # Startup - 2021 Data Analysis

# #### From a Finacial Newspaper

# The government has recognised 41,061 startups as of December 23, 2020, according to the Economic Survey 2020-21 tabled in Parliament on Jan 29,2021. Of this, more than 39,000 startups have reported 4,70,000 jobs,
# ndia currently houses the world's third largest startup ecosystem, with 38 firms being valued at over 1 billion dollars, 

# the government has taken several measures to support startups, including broadening the definition of startups, simplifying regulations, providing income tax exemptions and setting up a Rs 10,000 crore Fund of Funds for startups operated by the Small Industries Development Bank of India (Sidbi).

# ### importing the necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Load data

# In[2]:


#read the file
df=pd.read_csv(r"C:\Desktop\Data Analyst Project\startup 21\2021_registered_companies.csv")


# In[3]:


#data information
df.info()


# here we have 12 columns and 58893 rows in the dataset ,which contains 9 object datatype and 3 float data type

# Column name meaning xplaination:
# 
# this dataset consists fo all the registered companies in period of January-21 to April-21
# 
# company_uid -a unique id given to every comapany registered.
# 
# date_of_registeration - Date on which the company was registered.
# 
# month_name -Month on which the company was registered.
# 
# State -State in which the company was registered.
# 
# roc - The Registrar of Companies ( ROC ) is an office under the Ministry of Corporate Affairs (MCA), which is the body that deals with the administration of companies and Limited Liability Partnerships in India. Basically this column contains information about the city of ROC.
# 
# Category -Defines the Category of the company.
# 
# class -Defines class of a comapny.
# 
# comapny_type -define type of the comapny.
# 
# activity_description - defines what business the comapny is into.

# In[ ]:





# In[4]:


df.describe()


# In[5]:


##checking the number of null values  in each column
df.isna().sum()


# we can see here here there is no null values in the data,

# In[6]:


df.shape


# #### Changing the data type of columns from float ot integer type

# In[7]:


df['authorized_capital']=df['authorized_capital'].astype('int')
df['paidup_capital']=df['paidup_capital'].astype('int')
df['activity_code']=df['activity_code'].astype('int')


# here we have successfully converted columns authorized capital & paidup capital to float to integer data type

# In[8]:


df.columns


# #### Removing the extra columns from data

# In[9]:


df.drop('activity_code',axis=1,inplace=True)


# In[10]:


#display top 10 records
df.head(10)


# ## How many companies were  registered each in months of 2021

# In[11]:


#group months
df.groupby('month_name')['company_uid'].count()


# In[12]:


ax=sns.countplot(data=df,x='month_name')
plt.title('Total companies registered')
plt.xlabel('Months')
plt.ylabel('companies registered')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# we can see here highest registration done on march month 17324,and after this feb,apr and january months  the number  registration are 14092,12554 and 10924 respectively

# ### Number of companies registered in each states

# In[14]:


df.groupby('state')['company_uid'].count().keys()


# as the state names are present in short form and full name
# first we need to change everyone in sigle format

# In[15]:


#Denoting short form into long form
short ={'MH':  'Maharashtra'
,'TG': 'Telangana'
,'GJ': 'Gujarat'
,'CH': 'Chandigarh'
,'DL': 'Delhi'
,'HR': 'Haryana'
,'UP': 'Uttar Pradesh'
,'RJ': 'Rajasthan'
,'CT': 'Chattisgarh'
,'KL': 'Kerala'
,'WB': 'West Bengal'
,'KA': 'Karnataka'
,'MP': 'Madhya Pradesh'
,'PB': 'Punjab'
,'BR': 'Bihar'
,'MN': 'Manipur'
,'TN': 'Tamil Nadu'
,'OR': 'Orissa'
,'HP': 'Himachal Pradesh'
,'UR': 'Uttarakhand'
,'JH': 'Jharkhand'
,'AP': 'Andhra Pradesh'
,'GA': 'Goa'
,'AS': 'Assam'
,'DN': 'Dadra & Nagar Haveli'
,'TR': 'Tripura'
,'JK': 'Jammu & Kashmir'
,'PY': 'Pondicherry'
,'MZ': 'Mizoram'
,'NL': 'Nagaland'
,'AN': 'Andaman & Nicobar'
,'AR': 'Arunachal Pradesh'
,'LD': 'Lakshadweep'
,'ML': 'Meghalaya'
,'LH': 'Jammu & Kashmir'
,'DD': 'Daman and Diu'
     }


# In[16]:


#here merging the data
df.replace({'state':short},inplace=True)


# In[19]:


s=df['state'].value_counts().sort_values(ascending=False)
s


# In[19]:


plt.figure(figsize=(8,20))
ax=sns.countplot(data=df,y='state')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xlabel('number of startups')
        


# we can ,see here most startup registered state is maharashtra,with 10077 startups
# and in second place uttarpradesh with 5772 startups,
# Delhi,Karnataka & Telangana are from third to fifth place with 3655 to 5449 

# In[ ]:





# ### Explore the  number of  registration of each months based on class

# In[21]:


plt.figure(figsize=(9,5))
ax=sns.countplot(data=df,x='month_name',hue='class')
for bars in ax.containers:
    ax.bar_label(bars)


# as showed in above graph, the startup type from jan-21 to apr-21, the  classtype not increasing steadily with months  but still the private startup  values are much higher than the other two's in each month,
# the highest startups private 15879 ,public 368 and private (one person company) 1077 startups are on march .
# and the least one on jan -21 with private 10085 ,public 243 and private (one person company) 596 startups

# ### Determine on which date the highest Registration of startups done ?

# In[22]:


df.groupby(['date_of_registration']).size().sort_values(ascending=False)


# In[23]:


plt.figure(figsize=(8,34))
ax=df['date_of_registration'].value_counts().plot(kind='barh',color='green')
for bars in ax.containers:
    ax.bar_label(bars)

from the above graph we can say the that the highest registrations 926 were on  8-2-21, the second highest on 16-3-21 & the least one on 27-3-21 with 1
so we cant predict the exactly trend  like its continuasly increasing or decreasing with time bcz there area lot factors bcz that the registration might affect
# ### Determine monthly Number of registration ,category-wise.

# In[17]:


plt.figure(figsize=(9,4))
ax=sns.countplot(data=df,x='month_name',hue='category')
for bars in ax.containers:
    ax.bar_label(bars)


# here we can see march month have highest registration in both category company limited by shares and company limited by guarantee,
# now coming to numerical term , in march company limited by share is 17216  and company limited by guarantee is 108 respectively

# # what is the Number of registration per day 

# In[18]:


plt.figure(figsize=(9,7))
plt.figure(figsize=(8,34))
ax=df['date_of_registration'].value_counts().plot(kind='barh')
for bars in ax.containers:
    ax.bar_label(bars)


# ### Determine the Registration by company type?

# In[26]:


com=df['company_type'].value_counts()
com


# In[20]:


plt.figure(figsize=(7,4))
ax=sns.countplot(data=df,y='company_type')
for bars in ax.containers:
    ax.bar_label(bars)


# here we can see non govt companies have highest registration 54389  and after this subsidiary of foriegn companies  have 430 registration and  with 6 registations union govt company in least registration

# ### determine monthly registrations  of non goverment companies

# In[21]:


df[df['company_type']=='Non-govt company']['month_name'].value_counts()


# In[29]:


ngo=df[df['company_type']=='Non-govt company']
month=ngo['month_name'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(month,autopct='%.2f%%',labels=month.index)


# we can see here in graph highest number of registrations is 17155 from march. and then 13972,12432 and 10830 from from feb ,april and january respectively

# ### Registraion Distribution in jan month

# In[24]:


df[df['month_name']=='Jan-21']['company_type'].value_counts()


# In[41]:


jan=df[df['month_name']=='Mar-21']
company=jan['company_type'].value_counts()
plt.pie(company,autopct='%.02f%%',labels=company.index)


# we can see here the highest number of registration in january month  is 10830 from Non govt companies and then from subsidiary of foriegn companies from 

# ### number of registration from state govt companies

# In[27]:


df[df['company_type']=='State Govt company']['state'].value_counts()


# In[26]:


df[df['company_type']=='State Govt company']['state'].value_counts().plot(kind='pie',autopct='%.2f')


# as we can see here orrisa and tamilnadu have 4,4 registration and karnataka & kerala have 2,2 ,after this remaining have 1 ,1 1, 1 .

# ### which states have most  foriegn companies

# In[33]:


df[df['company_type']=='Subsidiary of Foreign Company']['state'].value_counts()

as we can see here karnataka have 105 most of the foriegn company and after this Maharastra have 88 companies
# ### Capital raised by foriegn company in india

# In[72]:


df[df['company_type']=='Subsidiary of Foreign Company']['paidup_capital'].sum()


# In[78]:


df.groupby(['company_type'])['paidup_capital'].sum()


# In[83]:


plt.figure(figsize=(6,7))

ax=sns.barplot(data=df[df['company_type']=='Subsidiary of Foreign Company'],x='paidup_capital',y='activity_description')
for bars in ax.containers:
    ax.bar_label(bars)


# as we can see here non govt company have highest capital 10 billion but if we talk about foriegn companies they have 4 billion capital

# ### distribution of non govt companies capital on different sectors

# In[87]:


plt.figure(figsize=(4,7))

ax=sns.barplot(data=df[df['company_type']=='Non-govt company'],x='paidup_capital',y='activity_description')
for bars in ax.containers:
    ax.bar_label(bars)


# ### which states have most guarantee and association companies

# In[34]:


df[df['company_type']=='Guarantee and Association comp']['state'].value_counts()


# In[33]:


df[df['company_type']=='Guarantee and Association comp']['state'].value_counts().plot(kind='pie',autopct='%.2f%%')


# maharashtra have most of the guarantee and association companies

# In[35]:


df['activity_description'].value_counts()


# # Registered companies of diffrent sectors 

# In[36]:


df['activity_description'].value_counts()


# In[36]:


plt.figure(figsize=(13,9))
ax=sns.countplot(data=df,y='activity_description')
for bars in ax.containers:
    ax.bar_label(bars)


# as we can see here higher number of companies were registered in business services which is around 15000 and in second place 
# community personal and  social services which is 7000 respectively

# ### top 10 sectors with most companies registered

# In[38]:


df['activity_description'][:10].value_counts().plot(kind='pie',autopct='%.2f%%')


# ### In which roc city  higher number of registration done

# In[21]:


df['roc'].value_counts()


# In[38]:


plt.figure(figsize=(7,8))
ax=sns.countplot(data=df,y='roc')
for bars in ax.containers:
    ax.bar_label(bars)


# we can see here delhi ios top place with 8154 and after this mumbai on second place with 6788 registrations

# ### Registration based on class

# In[39]:


df['class'].value_counts()


# In[31]:


df['class'].value_counts().plot(kind='pie',autopct='%.2f%%')


# #### Registration based on company type

# In[41]:


df['company_type'].value_counts()


# In[45]:


df['company_type'].value_counts().plot(kind='bar')


# higher number of registration in private type

# In[ ]:




