#!/usr/bin/env python
# coding: utf-8

# In[34]:


from json import loads,dump


# In[14]:


# Opening JSON file 
with open('source_file_2.json','r+') as file:
    data = loads(file.read())


# In[ ]:





# In[16]:


newlist = sorted(data, key=lambda k: k['priority'])


# In[ ]:





# In[30]:


manager = {}
watcher = {}
for datas in newlist:
    for managers in datas['managers']:
        if managers in manager:  
            manager[managers].append(datas['name'])
        else:
            manager[managers]=[]
            manager[managers].append(datas['name'])
    for watchers in datas['watchers']:
        if watchers in watcher:  
            watcher[watchers].append(datas['name'])
        else:
            watcher[watchers]=[]
            watcher[watchers].append(datas['name'])


# In[37]:


with open('manager.json', 'w') as outfile:
    dump(manager, outfile)


# In[36]:


with open('watcher.json', 'w') as outfile:
    dump(watcher, outfile)


# In[ ]:




