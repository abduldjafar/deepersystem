#!/usr/bin/env python
# coding: utf-8

# In[34]:


from json import loads,dump


# Opening JSON file 
with open('source_file_2.json','r+') as file:
    data = loads(file.read())

newlist = sorted(data, key=lambda k: k['priority'])

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

with open('manager.json', 'w') as outfile:
    dump(manager, outfile)

with open('watcher.json', 'w') as outfile:
    dump(watcher, outfile)


