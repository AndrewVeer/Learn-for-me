#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Множества
s=set() #создание пустого множества
basket={'apple','orange','apple','pear',
'orange','banana'}
print(basket) #{'orange','apple','banana','pear'}
'orange' in basket #True
'python' in basket #False
#Операции с множествами
s.add(element) #добавление элемента в множество
s.remove(element) #удаление элемента, если нет во множестве будет ошибка
s.discard(element) #удаление элемента без ошибки
s.clear() #удалить все элементы из множества
#Перебор элементов множества
basket={'apple','orange','apple','pear','orange','banana'}
for x in basket:
print(x)

banana
apple
orange
pear


# In[3]:


#Словари
#Словарь (dictionary), отображение (map),
#ассоциативный массив.
#Позволяет хранить пары <ключ, значение>.
dict,{}
d={'a':239,10:100}
print(d['a'])
print(d[10])
#Операции со словарями
key in dictionary
key not in dictionary
dictionary[key]=value
dictionary[key]
dictionary.get(key) #вернет значение, либо None, если ключа такого нет, без ошибки
del dictionary[key]
#Словари
#Изменяяемы
#Элементы не имеют порядка
#Все ключи различны
#Ключи неизменяемы
#Ключами могут быть строки, числа...
#Ключами не могут быть списки, другие словари


# In[4]:


#Перебор элементов словаря
d={'C':14,'A':12,'T':9,'G':18}
for key in d:
   print(key,end='') #C A T G
for key in d.keys():
   print(key,end='') #C A T G
for value in d.values():
   print(value,end='') #14 12 9 18
for key,value in d.items():
   print(key,value,end='') #C 14; A 12; T 9; G 18


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




