# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:06:49 2021

@author: gupta
"""
import matplotlib.pyplot as plt
f=open("_chat.txt", encoding='utf-8')
names={}
for i in f.readlines()[1:]:
    if ": " in i and "]" in i and "changed the subject to" not in i:
        name=i[i.find("]")+2:i.find(": ")]
        if name not in names:
            names[name]=1
        else:
            names[name]+=1      
names.pop('')
namelist=[i for i in names]; namemessage=[names[i] for i in namelist]
namelist=[i.split()[0] for i in namelist]
plt.title('losers message frequency')
plt.xlabel('Person')
plt.ylabel('Number of messages')
plt.xticks(rotation=90)
plt.bar(namelist,namemessage)
plt.savefig('losers message')