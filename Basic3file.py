#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Чтение из файла
inf = open('file.txt','r')  #open('file.txt')
s1 = inf.readline()
s2 = inf.readline()
inf.close

with open('text.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
    
#здесь файл уже закрыт


# In[ ]:


#Пара полезных функций
s= inf.readline().strip()
'\t abc  \n'.strip() -> 'abc'

os.path.join('_','dirname','filename.txt')
'_\dirname\filename.txt'


# In[ ]:


#Построчное чтение файла
with open('input.txt') as inf:
    for line in inf:
        line=line.strip()
        print(line)


# In[ ]:


#Запись в файл
ouf=open('file.txt','w')
ouf.write('Somme text\n')
ouf.write(str(25))
ouf.close

with open('text.txt','w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))
    
#здесь файл уже закрыт


# In[22]:


with open('d:\Basic\dataset_3363_2.txt','r') as inf:
    a=inf.readline()
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
for i in range(len(b)):
    print(b[i]*int(c[i]),end)
#with open('d:\Basic\output.txt','w') as ouf:
#    ouf.write(d)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




