#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=5
while a>0:
    print(a,end=' ')
    a-=1


# In[5]:


a=5
while a<=55:
    print(a,end=' ')
    a+=2


# In[10]:


a=5
while a<=55:
    if a%2==1:
        print(a,end=' ')
    a+=1


# In[21]:


i=0
while i<=10:
    i+=1
    if i>7:
        i+=2
    print(i,end=' ')


# In[29]:


n=int(input())
a=1
while a<=n:
    print('*'*a)
    a+=1


# In[30]:


n=int(input())
s='*'
while len(s)<=n:
    print(s)
    s+='*'


# In[33]:


i=0
while i<5:
    print('*',end='')
    if i%2==0:
        print('**')
    if i>2:
        print('***')
    i+=1


# In[43]:


a,b=int(input()),int(input())
s=0
while a<=b:
    s+=a
    a+=1
print(s)


# In[61]:


s=int(input())
i=0
while s!=0:
    i+=s
    s=int(input())
S=i
print(S)


# In[87]:


a,b,d=int(input()),int(input()),a
while d%b!=0:
    d+=a
print(d)


# 

# In[92]:


#предпочтительнее: меньше итераций в коде, меньше съедает ОЗУ
a,b=int(input()),int(input())
if   a > b:
    p = a 
    while p % b != 0: p += a
elif a < b:
    p = b
    while p % a != 0: p += b
else: p = a
print (p)


# In[ ]:




