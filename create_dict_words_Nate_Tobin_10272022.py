#!/usr/bin/env python
# coding: utf-8

# In[5]:


doc = open('C:\GIS\words.txt')

def create_dict_words():
    words_dict = dict()
    for l in doc:
        words = l.strip()
        words_dict[words] = words
    return words_dict


# In[6]:


create_dict_words()


# In[ ]:




