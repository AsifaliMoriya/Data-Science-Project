#!/usr/bin/env python
# coding: utf-8

# # Telecom Data Analysis

# DataSet Info : Telecom Customer Churn and Revenue Prediction

# In[1]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.ticker as mtick  
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


cd C:\Users\asifa\OneDrive\Desktop\Telecomes Project


# In[3]:


telecom_data = pd.read_csv("telecom.csv")


# In[4]:


telecom_data.head()


# In[5]:


telecom_data.shape


# In[6]:


telecom_data.columns.values


# In[7]:


#Checking Data Types
telecom_data.dtypes


# In[8]:


# Check the descriptive statistics of numeric variables
telecom_data.describe()


# Insight :
# 
# SeniorCitizen is actually a categorical hence the 25%-50%-75% distribution is not proper
# 
# 75% customers have tenure less than 55 months
# 
# Average Monthly charges are USD 64.76 whereas 25% customers pay more than USD 89.85 per month

# In[9]:


telecom_data['Churn'].value_counts().plot(kind='barh', figsize=(8, 6))
plt.xlabel("Count", labelpad=14)
plt.ylabel("Target Variable", labelpad=14)
plt.title("Count of TARGET Variable per category", y=1.02);


# In[10]:


#Getting Churn Rate in Percentage(%)
telecom_data['Churn'].value_counts()/len(telecom_data['Churn'])*100


# In[11]:


#Getting Churn Rate in Values
telecom_data['Churn'].value_counts()


# Data is highly imbalanced, ratio = 73:27 , 
# So we analyse the data with other features while taking the target values separately to get some insights.

# In[12]:


# Concise Summary of the dataframe because we have too many columns we are using the verbose = True mode
telecom_data.info(verbose = True)


# Here we can see that there is no null value so we can further proceed to the next step of data cleaning

# ## Data Cleaning

# Creating a copy of base data for manupulation & processing

# In[13]:


telecom_data = telecom_data.copy()


# Total Charges should be numeric Value Let's convert it to numerical data type

# In[14]:


telecom_data.TotalCharges = pd.to_numeric(telecom_data.TotalCharges, errors='coerce')
telecom_data.isnull().sum()


# As we can see there are 11 missing values in TotalCharges column because we have converted the data type object to int let's take a look at missing value data.

# In[15]:


telecom_data.loc[telecom_data ['TotalCharges'].isnull() == True]


# Since the % of these records compared to total dataset is very low that is 0.15%, it is safe to ignore them from further processing.

# In[16]:


#Removing missing values 
telecom_data.dropna(how = 'any', inplace = True)


# Dividing the customer on the base of their tenure so we can easily analysis the data.

# In[17]:


# Getting the max tenure months
print(telecom_data['tenure'].max()) #72


# In[18]:


labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]

telecom_data['tenure_group'] = pd.cut(telecom_data.tenure, range(1, 80, 12), right=False, labels=labels)


# In[19]:


telecom_data['tenure_group'].value_counts()


# Removing columns not required for further processing that creates no impact on model

# In[20]:


#drop column customerID and tenure
telecom_data.drop(columns= ['customerID','tenure'], axis=1, inplace=True)
telecom_data.head()


# ## Data Exploration

# Plot distibution of individual factor(columns) by churn

# In[21]:


for i, predictor in enumerate(telecom_data.drop(columns=['Churn', 'TotalCharges', 'MonthlyCharges'])):
    plt.figure(i)
    sns.countplot(data=telecom_data, x=predictor, hue='Churn')


# ## Feature Scaling

# Convert the target variable 'Churn'  in a binary numeric variable i.e. Yes=1 ; No = 0

# In[22]:


telecom_data['Churn'] = np.where(telecom_data.Churn == 'Yes',1,0)


# In[23]:


telecom_data.head()


# Converting all the categorical variables into dummy variables

# In[24]:


telecom_data_dummies = pd.get_dummies(telecom_data)
telecom_data_dummies.head()


# Plotting Relationship between Monthly Charges and Total Charges

# In[25]:


sns.lmplot(data=telecom_data_dummies, x='MonthlyCharges', y='TotalCharges', fit_reg=False)


# we can see that Total Charges increase as Monthly Charges increase - as expected.

# Churn by Monthly Charges and Total Charges

# In[26]:


Mth = sns.kdeplot(telecom_data_dummies.MonthlyCharges[(telecom_data_dummies["Churn"] == 0) ],
                color="Green", shade = True)
Mth = sns.kdeplot(telecom_data_dummies.MonthlyCharges[(telecom_data_dummies["Churn"] == 1) ],
                ax =Mth, color="Red", shade= True)
Mth.legend(["No Churn","Churn"],loc='upper right')
Mth.set_ylabel('Density')
Mth.set_xlabel('Monthly Charges')
Mth.set_title('Monthly charges by churn')


# Insight: As clearly seen that Churn is high when Monthly Charges ar high

# In[27]:


Mth = sns.kdeplot(telecom_data_dummies.TotalCharges[(telecom_data_dummies["Churn"] == 0) ],
                color="Green", shade = True)
Mth = sns.kdeplot(telecom_data_dummies.TotalCharges[(telecom_data_dummies["Churn"] == 1) ],
                ax =Mth, color="Red", shade= True)
Mth.legend(["No Churn","Churn"],loc='upper right')
Mth.set_ylabel('Density')
Mth.set_xlabel('Total Charges')
Mth.set_title('Total charges by churn')


# Insight : Higher the Total Charges , Higher the Churn rate

# However if we combine the insights of 3 parameters of Tenure, Monthly Charges & Total Charges then the analysis is bit clear that Higher Monthly Charge at lower tenure results into higher Total Charge. Hence, all these 3 factors i.e Higher Monthly Charge, Lower tenure and Higher Total Charge are linked to High Churn.

# Checking Corelation between Variable with 'churn'

# In[28]:


plt.figure(figsize=(20,8))
telecom_data_dummies.corr()['Churn'].sort_values(ascending = False).plot(kind='bar')

Derived Insight :

High Churn Factors:

Month-to-month contracts
Lack of online security and tech support
First year of subscription
Fiber optics internet service

Low Churn Factors:

Long-term contracts
Subscriptions without internet service
Customers engaged for 5+ years

Factors with Minimal Impact on Churn:

Gender
Availability of phone service
Number of multiple lines

It's good to see such clear patterns emerge, as this insight can inform strategies to reduce churn and improve customer retention.
# In[29]:


plt.figure(figsize=(12,12))
sns.heatmap(telecom_data_dummies.corr(), cmap="Paired")


# ## Bivariate Analysis

# Seprating the target value as Churn and Not Churn so we can analyze the churn customer and non churn customer

# In[30]:


new_df1_target0=telecom_data.loc[telecom_data["Churn"]==0]
new_df1_target1=telecom_data.loc[telecom_data["Churn"]==1]


# Defining Uniplot so we can use all the properties for further Chart work

# In[31]:


def uniplot(df,col,title,hue =None):
    
    sns.set_style('whitegrid')
    sns.set_context('talk')
    plt.rcParams["axes.labelsize"] = 20
    plt.rcParams['axes.titlesize'] = 22
    plt.rcParams['axes.titlepad'] = 30
    
    
    temp = pd.Series(data = hue)
    fig, ax = plt.subplots()
    width = len(df[col].unique()) + 7 + 4*len(temp.unique())
    fig.set_size_inches(width , 8)
    plt.xticks(rotation=45)
    plt.yscale('log')
    plt.title(title)
    ax = sns.countplot(data = df, x= col, order=df[col].value_counts().index,hue = hue,palette='bright') 
        
    plt.show()


# In[32]:


uniplot(new_df1_target1,col='Partner',title='Distribution of Gender for Churned Customers',hue='gender')


# In[33]:


uniplot(new_df1_target0,col='Partner',title='Distribution of Gender for Non Churned Customers',hue='gender')


# In[34]:


uniplot(new_df1_target1,col='PaymentMethod',title='Distribution of PaymentMethod for Churned Customers',hue='gender')


# In[35]:


uniplot(new_df1_target0,col='PaymentMethod',title='Distribution of PaymentMethod for Non Churned Customers',hue='gender')


# In[36]:


uniplot(new_df1_target1,col='Contract',title='Distribution of Contract for Churned Customers',hue='gender')


# In[37]:


uniplot(new_df1_target0,col='Contract',title='Distribution of Contract for Non Churned Customers',hue='gender')


# In[38]:


uniplot(new_df1_target1,col='TechSupport',title='Distribution of TechSupport for Churned Customers',hue='gender')


# In[39]:


uniplot(new_df1_target0,col='TechSupport',title='Distribution of TechSupport for Non Churned Customers',hue='gender')


# In[40]:


uniplot(new_df1_target1,col='SeniorCitizen',title='Distribution of SeniorCitizen for Churned Customers',hue='gender')


# In[41]:


uniplot(new_df1_target0,col='SeniorCitizen',title='Distribution of SeniorCitizen for Non Churned Customers',hue='gender')


# In[42]:


telecom_data_dummies.to_csv('telecom_churn.csv')


# ## Conclusion
These insights are quite revealing:

Electronic Check Medium: It's interesting that customers using electronic checks exhibit higher churn rates. This could indicate potential issues with payment processing or dissatisfaction with billing methods.

Contract Type - Monthly: The absence of contract terms for monthly customers likely contributes to higher churn rates, as they have more flexibility to switch providers without penalty. Implementing incentives or strategies to encourage longer-term commitments could help mitigate this churn.

No Online Security, No Tech Support: The correlation between lack of online security and tech support with higher churn rates underscores the importance of these services in customer satisfaction and retention. Strengthening these aspects of service provision could help reduce churn.

Non-Senior Citizens: It's intriguing that non-senior citizens exhibit higher churn rates. Understanding the specific needs and preferences of this demographic group could be crucial in tailoring retention strategies effectively.

Identifying these trends allows for targeted interventions to address the underlying reasons for churn, potentially leading to improvements in customer retention and overall business performance.
# In[ ]:




