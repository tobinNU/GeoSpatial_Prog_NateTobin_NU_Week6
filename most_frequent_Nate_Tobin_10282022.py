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


# In[45]:


most_frequent("Hello break down the letters for me please.")


# In[46]:


most_frequent("Es un placer conocerte, ¿Cómo te llamas?")


# In[44]:


most_frequent(" Toute personne a droit à l'éducation. L'éducation doit être gratuite, au moins en ce qui concerne l'enseignement élémentaire et fondamental.")


# In[42]:


most_frequent("تصحبك السلامة")


# In[43]:


most_frequent("祝你今天过得愉快")


# In[ ]:




