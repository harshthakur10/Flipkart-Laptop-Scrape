#!/usr/bin/env python
# coding: utf-8

# # The objective of this task is to scrape details of laptops from Flipkart using Beautiful Soup and Selenium. This involves extracting information such as the name, price, ratings, and specifications of various laptops listed on Flipkart.Set up a Python environment with Beautiful Soup and Selenium installed. Write a script to scrape laptop details from Flipkart
# 

# In[2]:


pip install selenium


# In[3]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[8]:


driver= webdriver.Chrome()
driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g")


# In[9]:


soup=BeautifulSoup(driver.page_source,'html.parser')
soup


# In[11]:


n = "_4rR01T"

p = "_30jeq3 _1_WHN1"

r = "_3LWZlK"


# In[12]:


laptop_names=soup.find_all(class_=n)
laptop_prices=soup.find_all(class_=p)
laptop_rating=soup.find_all(class_=r)


# In[13]:


ln=[]
for i in laptop_names:
    ln.append(i.text)
    
lp=[]
for i in laptop_prices:
    lp.append(i.text)

lr=[]
for i in laptop_rating:
    lr.append(i.text)


# In[14]:


ln


# In[15]:


lp


# In[16]:


lr


# In[17]:


d.quit


# In[ ]:




