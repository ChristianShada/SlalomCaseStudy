#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Import Libraries
import pandas as pd
import os
import io
import numpy as np
import csv


# In[37]:


# Read in CSV Files
Weather=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/seattleWeather_1948-2017.csv')
Reviews=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/reviews.csv')
Listings=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/listings.csv')
Calendar=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/calendar.csv')


# ## Weather

# In[38]:


#Print Weather Data
Weather


# In[39]:


#Grab 2016 Data
Weather2016 = Weather[Weather['DATE'].str.contains('2016')]
Weather2016


# In[40]:


#Parce out January data to ensure accuracty
Weather012016 = Weather2016[Weather2016['DATE'].str.contains('2016-01')]
Weather012016.head()


# In[41]:


#Find Average Weather of TMAX/TMIN column to ensure accuracy
TMAX012016Ave = Weather012016["TMAX"].mean()
TMIN012016Ave = Weather012016["TMIN"].mean()
print(TMAX012016Ave)
print(TMIN012016Ave)


# In[ ]:


#Convert data to show 2016 results and export to CSV
Weather2016 = Weather[Weather['DATE'].str.contains('2016')]
Weather2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Weather2016.csv', index=False)


# ## Listing

# In[42]:


# Create Condenced Columns within the "listings.csv"
CondencedListings = pd.read_csv("Desktop/SlalomCaseStudy/Data_Files/listings.csv", usecols=['id', 'host_id', 'availability_30', 'availability_60', 'availability_90', 'latitude', 'longitude', 'has_availability'])


# In[43]:


#Print to table
CondencedListings.head()


# In[ ]:


# Condencing Listing data to only 2016
Listing2016 = Listings[Listings['last_scraped'].str.contains('2016')]
Listing2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Listing2016.csv', index=False)


# ## Calendar

# In[59]:


#Print Calendar 
Calendar


# In[49]:


# To Ensure accuracy of what IS and what IS NOT available
Calendar['available'].value_counts()


# In[ ]:


#Convert data to show 2016 results and export to CSV
Calendar2016 = Calendar[Calendar['date'].str.contains('2016')]
Calendar2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Calendar2016.csv', index=False)


# #### I did not use results data too much in my data analysis, however I thought it important to parce out 2016 as well.

# In[108]:


#Convert data to show 2016 results and export to CSV
Reviews2016 = Reviews[Reviews['date'].str.contains('2016')]
Reviews2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Reviews2016.csv', index=False)

