#!/usr/bin/env python
# coding: utf-8

# In[38]:


def most_frequent(sample):
    h = {}
    for x in sample:
        h[x] = h.get(x, 0) + 1

    t = []
    for x, freq in h.items():
        t.append((freq, x))

    t.sort(reverse=True)

    return t


# In[39]:


most_frequent("Hello break down the letter")


# In[40]:


most_frequent("Si Señor")


# In[41]:


most_frequent("Bonjour Madame")


# In[42]:


most_frequent("تصحبك السلامة")


# In[43]:


most_frequent("祝你今天过得愉快")


# In[ ]:




