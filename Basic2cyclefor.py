#!/usr/bin/env python
# coding: utf-8

# In[3]:


for i in 2,3,5:
    print(i*i)


# In[4]:


for i in range (10):
    print (i*i)


# In[5]:


for i in range (2,5):
    print (i)


# In[6]:


for i in range (2,15,2):
    print(i,end=' ')


# In[108]:


for i in range (5+1):
    print(i,end=' ')


# In[9]:


n=int(input())
for i in range (n):
    print('*'*n)


# In[11]:


n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()


# In[208]:


a,b,c,d=int(input()),int(input()),int(input()),int(input())
if ((a<=b)and(c<=d))<=10:
    for j in range(c,d+1):
        print('\t',j,end='\t')
    print(sep='\n')              #print(sep='\n') пропускает 1 строку, а print('\n') - 2 строки
    for i in range(a,b+1):
        print(i,end='')
        for h in range(c,d+1):
            print('\t',h*i,end='\t')
        print()


# In[206]:


a,b,c,d=input().split()
a,b,c,d=int(a),int(b),int(c),int(d)
for i in range(a, b+1):
    print(i, end='') 
    for j in range(c, d+1):
        print('\t', i*j, end='\t')
    print()


# In[2]:


a,b=input().split()
a,b=int(a),int(b)
s=0
for i in range(a,b+1):
    if i%2==1:
        s+=i
print(s)


# In[3]:


a,b=input().split()
a,b=int(a),int(b)
s=0
if a%2==0:
    a+=1
for i in range(a,b+1,2):
    s+=i
print(s)


# In[9]:


a,b=(int(i)for i in input().split())
s=0
if a%2==0:
    a+=1
for i in range(a,b+1,2):
    s+=i
print(s)


# In[16]:


a,b=int(input()),int(input())
s=0
S=0
for i in range(a,b+1):
    if i%3==0:
        s+=i
        S+=1
print(s/S)


# In[25]:


a,b=int(input()),int(input())
a += -a%3
b -= b%3
print((a+b)/2)


# In[ ]:




