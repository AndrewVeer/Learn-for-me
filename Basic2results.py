#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Поиск минимума в списке
пример 5 8 4 3 5 7
итог 3


# In[1]:


a=[int(i) for i in input().split()]
m=a[0]
for x in a:
    if m>x:
        m=x
print(m)


# In[ ]:


Сапер
Даны размеры поля для игры в сапер и координаты мин,
стоящих на этом поле. Вывести поле игры на экран.
Ввод             Вывод
5 4 4            *21.
1 1              3*2.
2 2              2*31
3 2              112*
4 4              ..11


# In[2]:


n,m,k=(int(i) for i in input().split())
a=[[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row,col=(int(i) -1 for i in input().split())
    a[row][col]=-1
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            for di in range(-1,2):
                for dj in range(-1,2):
                    ai=i+di
                    aj=j+dj
                    if 0<=ai<n and 0<=aj<m and a[ai][aj]==-1:
                        a[i][j]+=1
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            print('*',end='')
        elif a[i][j]==0:
            print('.',end='')
        else:
            print(a[i][j],end='')
    print()


# In[3]:


i,c=0,0
while True:
    s=int(input())
    i+=s
    c+=s**2
    if i==0:
        break
print(c)


# In[ ]:


s=[int(input())]
while sum(s)!=0:
    s.append(int(input()))
print(sum([i**2 for i in s]))


# In[ ]:


s = [0, 0, 1]
while s[2]:
    i = int(input())
    s = [s[0] + i, s[1] + i ** 2, s[0] + i]
print(s[1])


# In[6]:


a=int(input())
for i in range(1,a):
    print(i)


# In[ ]:





# In[10]:


n = int(input())
a = []
for i in range(1, n +1):
    c = min(i,n)
    n = n - c
    a += [i] * c
    if n <= 0:
        break
print(*a)


# In[11]:


n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])


# In[1]:


a=[int(i) for i in input(). split()]
b=int(input())
c=''
j=0
for i in a:
    if i==b:
        c=c+' '+str(j)
    j+=1
if len(c)==0:
    print('Отсутствует')
else:
    print(c)


# In[2]:


l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
for i in range(len(l)):
    if l[i]==x: print(i, end = ' ')


# In[ ]:


numbers = [int(i) for i in input().split()]
needed = int(input())
if needed not in numbers:
    print("Отсутствует")
else:
    [print(i, end=" ") for i, x in enumerate(numbers) if x == needed]


# In[ ]:


a=[int(i) for i in input().split()]
b=int(input())
if b in a:
    while b in a:
        print(a.index(b),end=' ')
        a[a.index(b)]=b+1  
else:
    print('Отсутствует')


# In[ ]:


matrix = []
s = input()
while s!='end':
    s = [int(x) for x in s.split()]
    matrix.append(s)
rows = len(matrix)
cols = len(matrix[0])
a = [[0 in range(cols):
		if i + 1 < rows and j + 1 < cols:
			a[i][j] = matrix[i][j-1]+matrix[i][j+1]+matrix[i-1][j]+matrix[i+1][j]
		elif i + 1 >= rows and j + 1 < cols:
			a[i][j] = matrix[i][j-1]+matrix[i][j+1]+matrix[i-1][j]+matrix[0][j]
		elif i + 1 < rows and j + 1 >= cols:
			a[i][j] = matrix[i][j-1]+matrix[i][0]+matrix[i-1][j]+matrix[i+1][j]
		else:
			a[i][j] = matrix[i][ for j in range(cols)] for i in range(rows)]
for i in range(rows):
	for jj-1]+matrix[i][0]+matrix[i-1][j]+matrix[0][j]
for t in a:
	for r in t:
		print (r, end=" ")
	print()


# In[8]:


n=int(input())
a=[[0 for i in range(n)] for j in range(n)]
i=0 #строки
j=0 #столбцы
x=1 #текущее значение для заполнения ячейки
k=0 #порядковый номер контура
while x<=n*n:
    a[i][j]=x
    if i!=j:
        a[j][i]=(a[k][k]+(n-k*2)*2)*2-4-x
    if j!=n-k-1:
        j+=1
    elif i!=n-k-1:
        i+=1
    elif x!=n*n:
        k+=1
        i=j=k
        x=a[k][k-1]
    x+=1
for i in a:
    print(*i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




