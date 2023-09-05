#!/usr/bin/env python
# coding: utf-8

# # Analysis of average number of smokers, by Age and by Gender

# In[2]:


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import statsmodels.api as sm


# In[3]:


url = "https://raw.githubusercontent.com/UMstatspy/UMStatsPy/master/NHANES/merged/nhanes_2015_2016.csv"
da = pd.read_csv(url)

da['SMQ020x'] = da.SMQ020.replace({1: 'Yes', 2: 'No', 7: np.nan, 9: np.nan})
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})


# In[4]:


da['RIAGENDRx']


# In[5]:


da['SMQ020x']


# In[6]:


dx = da[["SMQ020x", "RIDAGEYR", "RIAGENDRx"]].dropna() ### Eliminamos los 'na'


# ## Table of the average number of smokers by gender

# In[7]:


dx["SMQ020x"] = dx.SMQ020x.replace({'Yes': 1, 'No': 0}) ### regresamos a tener valores en lugar de 'str' para hacer calculos
### Tomamos la suma de 'Yes' = 1 y lo dividimos entre el 'n' total para obtener la proporción de fumadores
dz = dx.groupby('RIAGENDRx').agg({'SMQ020x': [np.mean, np.size]})
dz


# ## Table of the average number of smokers by Gender and by Age

# In[8]:


### Haremos una tabla divida por género, divididos por edad 
dx["SMQ020x"] = dx.SMQ020x.replace({'Yes': 1, 'No': 0}) ### regresamos a tener valores en lugar de 'str' para hacer calculos
dx['agegrp'] = pd.cut(dx.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
dx.groupby(['agegrp', 'RIAGENDRx']).agg({'SMQ020x': [np.mean, np.size]})


# ## Bar graph of the average number of smokers by Age

# In[11]:


plt.figure(figsize=(10, 6))
dx.groupby('agegrp')['SMQ020x'].agg(np.mean).plot(kind='bar', color = 'teal')
plt.title('Proportion of smokers per age')
plt.xlabel('Age groups')
plt.ylabel('Average number of smokers')
plt.xticks(rotation=45)
plt.show()


# ## Bar graph of the average number of smokers by Age and by Gender

# In[12]:


# Filtrar los datos por género
male_data = dx[dx['RIAGENDRx'] == 'Male']
female_data = dx[dx['RIAGENDRx'] == 'Female']

# Calcular el promedio de 'SMQ020x' por grupo 'agegrp' para ambos sexos
male_avg = male_data.groupby('agegrp')['SMQ020x'].mean()
female_avg = female_data.groupby('agegrp')['SMQ020x'].mean()

# Crear dos gráficas de barras separadas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6)) # Crear dos subplots

# Primera gráfica para Male
male_avg.plot(kind='bar', ax=ax1)
ax1.set_title('Proportion of smokers per age (Male)')
ax1.set_xlabel('Age Group')
ax1.set_ylabel('Average number of smokers')


# Segunda gráfica para Female
female_avg.plot(kind='bar', ax=ax2, color = 'maroon')
ax2.set_title('Proportion of smokers per age (Female)')
ax2.set_xlabel('Age Group')
ax2.set_ylabel('Average number of smokers')


plt.tight_layout()
plt.show()


# In[ ]:




