#!/usr/bin/env python
# coding: utf-8

# In[33]:


i=0
while i<5:
    a,b=input().split()   #ввод 2 переменных через пробел
    a=int(a)
    b=int(b)
    if (a==0) and (b==0):
        break
    print(a*b)
    i+=1


# In[9]:


i=0
while i<5:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if (a==0) and (b==0):
        break
    if (a==0) or (b==0):
        continue
    print(a*b)
    i+=1


# In[11]:


i=0
s=0
while i<10:
    i=i+1
    s=s+i
    if s>15:
        break
    i=i+1
print(i)


# In[12]:


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)


# In[31]:


while True:     #бесконечный цикл пока не встретится break
    s=int(input())
    if 10<=s<=100:
        print(s)
        continue
    if s>100:
        break


# In[26]:


b=''
while True:   #бесконечный цикл пока не встретится break
    a=int(input())
    if a<10: continue
    elif a>100: break
    else: b=b+str(a)+'\n'
print (b)


# In[28]:


while 1==1:
    a=int(input())
    if a>100: break
    if a<10: continue
    print (a)


# In[ ]:




