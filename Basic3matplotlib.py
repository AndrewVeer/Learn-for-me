#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *


# In[4]:


x=linspace(0,5,10)
y=x**2
print(x)
print(y)


# In[5]:


figure()
plot(x,y,'r') #'r' цвет линии
xlabel('x')
ylabel('y')
title('title')
show()


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


figure()
plot(x,y,'b')
xlabel('x')
ylabel('y')
title('parabola')
show()


# In[9]:


fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8]) #left, bottom, width, height (range 0 to 1)
axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title') #чтобы не отображалась строка <matplotlib.text.text at ...> в конце можно 


# In[11]:


fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8]) #main axes
axes2=fig.add_axes([0.2,0.5,0.4,0.3]) #inset axes
#main figure
axes1.plot(x,y,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
#insert figure
axes2.plot(y,x,'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');


# In[12]:


fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x,y,'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
fig.tight_layout()


# In[14]:


fig, axes=plt.subplots(figsize=(12,3))
axes.plot(x,y,'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');


# In[19]:


fig,ax=plt.subplots()
ax.plot(x,x**2, label='y=x**2')
ax.plot(x,x**3, label='y=x**2')
ax.legend(loc=2); #upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title');


# In[20]:


#построение гистограммы
from numpy import *
n=random.randn(100000) #функция из numpy
fig, axes=plt.subplots(1,2,figsize=(12,4))

axes[0].hist(n)
axes[0].set_title('Default histogram')
axes[0].set_xlim((min(n),max(n)));

axes[1].hist(n,cumulative=True,bins=50)
axes[1].set_title('Cumulative  detailed histogram')
axes[1].set_xlim((min(n),max(n)));


# In[ ]:




