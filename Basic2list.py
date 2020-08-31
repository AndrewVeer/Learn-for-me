#!/usr/bin/env python
# coding: utf-8

# In[1]:


students=['Ivan','Masha','Sasha']
for student in students:
    print('Hello, '+student+'!')


# In[ ]:


students[0]  'Ivan'
students[1]  'Masha'
students[2]  'Sasha'


# In[ ]:


students=['Ivan','Masha','Sasha']
Длина списка: len(students)
Результат: 3
students[0]  'Ivan'     students[-1] 'Sasha'
students[1]  'Masha'    students[-2] 'Masha'
students[2]  'Sasha'    students[-3] 'Ivan'

students[:2] - 0,1      students[::-1] - -1,-2,-3


# In[3]:


Операции со списками
+
students=['Ivan','Masha','Sasha']
teachers=['Oleg','Alex']
students+teachers
*
[0,1]*4
Результат: [0,1,0,1,0,1,0,1]


# In[ ]:


Изменение списков
В отличии от изученных типов данных (int,float,str)
списки  (list) являются изменяемыми

Можно изменить конкретный элемент списка:

students['Ivan','Masha','Sasha']
students[1]='Oleg'
print(students)
['Ivan','Oleg','Sasha']


# In[ ]:


Добавление элемнетов в список
students=['Ivan','Masha','Sasha']
students.append('Olga')
Результат:['Ivan','Masha','Sasha','Olga']
students+=['Olga']
Результат:['Ivan','Masha','Sasha','Olga','Olga']
students+=['Boris','Sergey']
Результат:['Ivan','Masha','Sasha','Olga','Olga','Boris','Sergey']


# In[ ]:


Вставка элементов в список
students=['Ivan','Masha','Sasha']
students.insert(1,'Olga')
Результат:['Ivan','Olga','Masha','Sasha']


# In[8]:


students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)


# In[ ]:


Удаление элемента из списка
students=['Ivan', 'Masha', 'Sasha']
students.remove('Sasha')
Результат:['Ivan','Masha']
del students[0]
Результат: ['Sasha']


# In[ ]:


Поиск элемента в списке
students=['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students:
print('Ivan is here!')
if 'Ann' not in students:
print('Ann is out')

ind=students.index('Sasha')
Результат: 2
ind=students.index('Ann')
Результат: ValueError:'Ann' is not in list


# In[ ]:


Сортировка списка
Не изменяя порядка изначального списка
students=['Sasha','Ivan', 'Masha']
ordered_students=sorted(students)
Результат: ['Ivan', 'Masha', 'Sasha']     min()
                                      max()
Изменяя сам список
students.sort()
Результат:['Ivan', 'Masha', 'Sasha']


# In[ ]:


Список в обратном порядке
students=['Sasha','Ivan', 'Masha']
students.reverse()
Результат:['Masha','Ivan', 'Sasha']

reversed(students)

students[::-1]


# In[ ]:


Присвоение списков
a=[1,'A',2]
b=a
a[0]=42
значение a:[42,'A',2]
значение b:[42,'A',2]
b[2]=30
значение b:[42,'A',30]
значение a:[42,'A',30]


# In[ ]:


Генерация списков
a=[0]*5                    [0,0,0,0,0]
a=[0 for i in range(5)]    [0,0,0,0,0]
a=[i*i for i in range(5)]  [0,1,4,9,16]
a=[int(i) for i in input().spilt()]  получаем список из чисел в исходной строке


# In[4]:


a=[int(i) for i in input().split()]
s=0
for i in range(len(a)):
    s+=int(a[i])
print(s)


# In[5]:


print(sum([int(i) for i in input().split()]))


# In[17]:


a=[int(i) for i in input().split()]
if len(a)==1:
    print(a[0])
else:
    for i in range(0,len(a)-1):
        print(a[i-1]+a[i+1],end=' ')
    print(a[len(a)-2]+a[0])


# In[19]:


a=[int(i) for i in input().split()]
if len(a)>1:
    for i in range(len(a)):
        print(a[i-1]+a[i+1-len(a)],end=' ')
else:
    print(a[0])


# In[ ]:


a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")


# In[4]:


a=[int(i) for i in input().split()]
a.sort()
s=[]
for i in range(len(a)):
    if i>0:
        if a[i]==a[i-1]:
            if s[i] not in s:
                s+=[a[i]]
for i in s:
    print(i, end=" ")


# In[ ]:


ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')


# In[ ]:


a = input().split()
b = list(set(a))
k=sorted(b)
for i in range(len(k)):
    c = a.count(k[int(i)])
    if c > 1:
        print(str(int(k[i])), end=' ')


# In[9]:


str = [int(i) for i in input().split()]
ans = []
[ans.append(x) for x in str if x not in ans and str.count(x) > 1]
print(*ans)


# In[ ]:


s = [int(i) for i in input().split()]
s.sort()
i = 0
while i < len(s):
    if s.count(s[i]) > 1:      # думаю, тут всё понятно
        print (s[i], end=' ')  
        i += s.count(s[i])     # прибавляем к индексу количество повторений текущего элемента,
                               # чтобы перескочить на первый отличающийся от текущего
    else:                      
        i += 1


# In[ ]:


Двумерные списки
a=[[1,2,3],[4,5,6],[7,8,9]]
a[1]=[4,5,6]
a[1][1]=5


# In[ ]:


Генерация двумерных списков
n=3
a=[[0]*n]*n  5 0 0
a[0][0]=5    5 0 0
a?           5 0 0

a=[[0]*n for i in range(n)] #каждый из этих списков будет независимым
a=[[0 for j in range(n)] for i in range(n)]


# In[ ]:




