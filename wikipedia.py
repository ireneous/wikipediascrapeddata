#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[9]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[10]:


print(soup)


# In[24]:


table = soup.find_all('table')[1] 
print(table)


# In[12]:


soup.find_all('table')[1]


# In[ ]:





# In[21]:


soup.find('table', class_='wikitable sortable')


# In[ ]:





# In[27]:


world_title = soup.find_all('th')


# In[28]:


print(world_title)


# In[46]:


world_title = soup.find_all('th')
world_title = [title.text.strip() for title in world_title]
print(world_title)


# In[36]:





# In[45]:


world_title = table.find_all('th')
print(world_title)


# In[ ]:





# In[50]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=world_title)
print(df)


# In[49]:





# In[57]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find_all('table', class_='wikitable sortable')[0]

headers = [th.text.strip() for th in table.find_all('tr')[0].find_all('th')]

print(headers)


# In[55]:


import pandas as pd
df = pd.DataFrame(columns = world_titles)


# In[58]:


table.find_all('tr')


# In[71]:


rows = table.find_all('tr')[1:]
data = []

for row in rows:
    cols = row.find_all(['td', 'th'])
    row_data = [col.text.strip() for col in cols]
    if len(row_data) == len(headers):
        data.append(row_data)

df = pd.DataFrame(data, columns=headers)
print(df)


# In[73]:


import os
print(os.path.expanduser('~'))


# In[74]:


df.to_csv('/Users/owner/Downloads/wikipedia.csv', index=False)


# In[ ]:




