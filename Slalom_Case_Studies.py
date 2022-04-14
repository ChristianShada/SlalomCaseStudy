#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import pandas as pd
import os
import io
import numpy as np
import csv


# In[2]:


# Read in CSV Files
Weather=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/seattleWeather_1948-2017.csv')
Reviews=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/reviews.csv')
Listings=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/listings.csv')
Calendar=pd.read_csv('Desktop/SlalomCaseStudy/Data_Files/calendar.csv')


# In[5]:


# Create Condenced Columns within the "listings.csv"
CondencedListings = pd.read_csv("Desktop/SlalomCaseStudy/Data_Files/listings.csv", usecols=['listing_id', 'host_id', 'availability_30', 'availability_60', 'availability_90', 'latitude', 'longitude'])


# In[13]:


#Print to table
CondencedListings.head()


# In[108]:


#Convert data to show 2016 results and export to CSV
Reviews2016 = Reviews[Reviews['date'].str.contains('2016')]
Reviews2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Reviews2016.csv', index=False)


# In[77]:


#Convert data to show 2016 results and export to CSV
Calendar2016 = Calendar[Calendar['date'].str.contains('2016')]
Calendar2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Calendar2016.csv', index=False)


# In[63]:


#Convert data to show 2016 results and export to CSV
Weather2016 = Weather[Weather['DATE'].str.contains('2016')]
Weather2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Weather2016.csv', index=False)


# In[16]:


Listing2016 = Listings[Listings['last_scraped'].str.contains('2016')]
Listing2016.to_csv('Desktop/SlalomCaseStudy/Data_Files/Listing2016.csv', index=False)


# In[ ]:




