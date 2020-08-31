#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Объявление функции
def min2(a,b):    def
if a<=b:      имя функции
    return a  аргументы (параметры)
else:         тело функции
    return b  return
#Вызов функции
#минимум из чисел 42,30
m=min2(42,30)
#минимум из чисел 42,30,25
m=min2(min2(42,30)25)
Функция должна быть объявлена ранее первого вызова


# In[7]:


def f(n):
    return n * 10 + 5
f(f(f(10)))


# In[ ]:


#Произвольное число параметров
def minimal(*a):   вызовы:
m=a[0]         minimal(5)
for x in a:    minimal(5,3)
    if m>x:    minimal(5,3,6,10)
        m=x    minimal([5,3,6,10])
return m


# In[ ]:


#Значения параметров по умолчанию
def my_range(start,stop,step=1) #print(my_range(2,5))
res=[]                      #[2,3,4]
if step>0:              #print(my_range(2,15,3))
    x=start             #[2,5,8,11,14]    
    while x<stop:       #print(my_range(15,2,-3))
        res+=[x]        #[15,12,9,6,3]
        x+=step
elif step<0:
    x=start
    while x>stop:       #my_range(stop=20,start=5)
        res+=[x]        #тоже будет работать корректно
        x+=step         #потому что указали сами переменные
return res              #start и stop


# In[ ]:


#Локальные переменные
def init_values():
a=100
b=200

init_values()
print(a+b)  #Ошибка, переменные a и b не объявлены


# In[ ]:


#Изменение локальных переменных
def init_values():       def init_values(a):
a=100                    a=100

a=0                      b=0
init_values()            init_values(b)
print(a)  #0             print(b)   #0


# In[ ]:


#Изменение объектов, связанных с локальными переменными
def append_zero(xs):
xs.append(0)

a=[]
append_zero(a)
print(a)  #[0]

def append_zero(xs):
xs.append(0)
xs=[100]

a=[]
append_zero(a)
print(a)  #[0]


# In[ ]:


#Глобальные переменные
def print_value():
print(a)

a=5
print_value()  # 5

#Глобальные и локальные переменные
def print_value():
print(a)
a=10
print(a)

a=5
print_value()
#UnboundLocalError: local variable 'a' referenced
#before assignment


# In[16]:


def f(x):
    if x<=-2:
        return 1-((x+2)**2)
    if -2<x<=2:
        return -(x/2)
    if x>2:
        return ((x-2)**2)+1


# In[ ]:


def modify_list(l):
    for i in reversed(range(len(l))): #запуск цикла с конца
        if l[i]%2 == 0:
            l[i] = l[i]//2
        else:
            del l[i]


# In[ ]:


def modify_list(l):
l[:]=[i//2 for i in l if i%2==0]


# In[ ]:





# In[ ]:





# In[ ]:




