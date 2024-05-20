#!/usr/bin/env python
# coding: utf-8

# # Customer Churn and Revenue Prediction Model

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from imblearn.combine import SMOTEENN
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import LinearRegression
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


cd C:\Users\asifa\OneDrive\Desktop\Telecom Project


# In[3]:


data = pd.read_csv('telecom_churn_analysis.csv')
data


# In[4]:


data = data.drop('Unnamed: 0',axis=1)
data


# ## Dividing data on the Basis of input and target Variable

# In[5]:


X = data.drop(columns=['Churn', 'TotalCharges'])
X


# In[6]:


y = data[['Churn','TotalCharges']]
y


# In[7]:


y1 = data['Churn']
y1


# In[8]:


y2 = data['TotalCharges']
y2


# ## Analyzing Corelation Between variable

# In[9]:


plt.figure(figsize = (30,30))
sns.heatmap(data.corr(), annot = True, cmap = "RdYlGn")

plt.show()


# In[10]:


selection = ExtraTreesRegressor()
selection.fit(X, y)


# In[11]:


print(selection.feature_importances_)


# In[12]:


plt.figure(figsize = (12,8))
feat_importances = pd.Series(selection.feature_importances_, index=X.columns)
feat_importances.nlargest(20).plot(kind='barh')
plt.show()


# ## Splitting the data and using SMOTEENN method for upsampling

# In[13]:


X_train, X_test, y1_train, y1_test, y2_train, y2_test = train_test_split(X, y1, y2, test_size=0.2, random_state=42)


# In[14]:


smote = SMOTEENN(random_state=42)
X_train_res, y_churn_train_res = smote.fit_resample(X_train, y1_train)


# In[15]:


Xr_train,Xr_test,yr1_train,yr1_test=train_test_split(X_train_res, y_churn_train_res,test_size=0.2)


# ## Using DecisionTreeClassifier for Churn Predction

# In[16]:


churn_model = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=6, min_samples_leaf=8)


# In[17]:


churn_model.fit(Xr_train,yr1_train)


# In[18]:


yr_predict = churn_model.predict(Xr_test)


# In[19]:


model_score_r = churn_model.score(Xr_test, yr1_test)


# In[20]:


model_score_r


# ## Using LinearRegression for Revenue Prediction

# In[21]:


revenue_model = LinearRegression()


# In[22]:


revenue_model.fit(X_train[y1_train == 0], y2_train[y1_train == 0])  # Only train on non-churned customers


# In[23]:


y_test_pred = revenue_model.predict(X_test)


# In[24]:


r2 = revenue_model.score(X_test, y2_test)
print(r2)


# ## Defining Function for user_input and for Predction of both Churn and Revenue

# In[25]:


def predict_churn_and_revenue(input_data):
    
    churn_prediction = churn_model.predict(input_data)
    if churn_prediction == 0:  # Customer does not churn
        revenue_prediction = revenue_model.predict(input_data)
    else:
        revenue_prediction = 0  # No revenue prediction if customer churns
    return churn_prediction, revenue_prediction


# In[26]:


input_data = X_test.iloc[44].values.reshape(1, -1)  

churn_prediction, revenue_prediction = predict_churn_and_revenue(input_data)

print(f"Churn prediction: {churn_prediction}")
if churn_prediction == 0:
    print(f"Predicted revenue if customer does not churn: {revenue_prediction}")
else:
    print("Customer is predicted to churn, no revenue prediction.")


# ## Saving Model

# In[56]:


import joblib

# Assuming you have two models: model1 and model2
models = {
     model1 :='churn_model',
     model2 :='revenue_model'
}

joblib.dump(models, 'models.pkl')


# In[ ]:




