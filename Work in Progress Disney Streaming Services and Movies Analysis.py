#!/usr/bin/env python
# coding: utf-8

# Goal of this project is to provide useful visual insights and EDA, as well as find out if rating/genre of movie are going to have an influence on the overall inflation adjusted gross revenue. This could be beneficial in order to find out if there should be further analysis done that would help Disney know more specifics about the ratings/genres of movie and the impact on their revenue brought in.

# In[51]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

disney = pd.read_csv('disney_plus_titles.csv')
disney_movies = pd.read_csv('disney_movies.csv')


# In[2]:


disney.head(10)


# In[4]:


disney.info()


# In[5]:


disney.shape


# In[6]:


disney.dtypes


# In[7]:


disney.isnull().sum()


# In[8]:


disney.describe()


# In[9]:


disney['type'].value_counts().to_frame()


# In[10]:


disney['listed_in'].value_counts().to_frame()


# disney_clean = disney.drop_duplicates(subset=['listed_in'])
# disney_clean.listed_in.unique()
# for i in range(len(disney_clean)):
#     dis_test = disney_clean['listed_in'][i].replace(',', '')
#     print (dis_test)

# In[12]:


sns.countplot(disney['type'])
plt.show()


# In[13]:


sns.countplot(disney['rating'])
plt.show()


# In[14]:


print(disney.release_year.min())
print(disney.release_year.max())


# In[50]:


x = sns.countplot(disney['release_year'])
sns.set(rc={'figure.figsize':(12,12)})
for index, label in enumerate(x.get_xticklabels()):
   if index % 4 == 0:
      label.set_visible(True)
   else:
      label.set_visible(False)
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
plt.show()


# In[20]:


disney.duration.value_counts().to_frame()


# In[21]:


disney.country.value_counts().to_frame()


# In[22]:


#y = sns.countplot(disney['type'])
#sns.set(rc={'figure.figsize':(12,12)})


pd.pivot_table(disney.reset_index(),
               index='release_year', columns='type'
              ).plot(subplots=True, xlabel = 'Year', ylabel = 'Count',title = 'Trendlines Over Time')


# In[24]:


disney_movies.head(10)


# In[25]:


disney_movies.info()


# In[46]:


disney_movies.groupby("genre").describe()


# In[47]:


print(disney_movies.nlargest(10, 'total_gross'))


# In[71]:


disney_movies['genre']=disney_movies['genre'].astype('category').cat.codes
disney_movies['mpaa_rating']=disney_movies['mpaa_rating'].astype('category').cat.codes
disney_movies.corr()


# In[73]:


new_list = []
disney_movies_clean = disney_movies.fillna(0)
movie_ratings = list(set(disney_movies_clean["mpaa_rating"]))
for x in movie_ratings:
    new_list.append(list(disney_movies_clean.where(disney_movies_clean["mpaa_rating"]==x).dropna()["inflation_adjusted_gross"]))


# In[74]:


stats.f_oneway(*new_list)


# In[75]:


list2 = []
genres = list(set(disney_movies_clean["genre"]))
for y in genres:
    list2.append(list(disney_movies_clean.where(disney_movies_clean["genre"]==y).dropna()["inflation_adjusted_gross"]))


# In[76]:


stats.f_oneway(*list2)


# Overall we found that there was some correlational information that encouraged me to take more of a look into how the ratings and genres might impact inflation adjusted gross values. We see that there is little correlation between these values; however, our data must be large enough to prove that the p-values are statisticall significant. This is a unique phenomenon and it could encourage further analysis and insight into what specific categories might be correlational and others that might not within our dataset. This would be next steps within the project to create better insight.
