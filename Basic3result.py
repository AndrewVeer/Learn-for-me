#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
x_list = [input().split(';') for x in range(n)]
vs = [(x[0], x[2]) for x in x_list]
import itertools
clubs = set(itertools.chain.from_iterable(vs))
res = {club:[0, 0, 0, 0, 0] for club in clubs}
for kom1, gol1, kom2, gol2 in x_list:
    res[kom1][0] += 1
    res[kom2][0] += 1
    if int(gol1) > int(gol2):
        res[kom1][1] += 1
        res[kom1][4] += 3
        res[kom2][3] += 1
    elif int(gol1) < int(gol2):
        res[kom2][1] += 1
        res[kom2][4] += 3
        res[kom1][3] += 1
    elif int(gol1) == int(gol2):
        res[kom1][2] += 1
        res[kom1][4] += 1
        res[kom2][2] += 1
        res[kom2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))


# In[ ]:


alf = input()
res_alf = input()

encode = input()
decode = input()

code = {}
decrypt = {}
for i in range(len(alf)):
    code.update([(alf[i], res_alf[i])])
    decrypt.update([(res_alf[i], alf[i])])

res_encode = []
for letter in encode:
    res_encode.append(code[letter])

print(''.join(res_encode))

res_decode = [decrypt[let] for let in decode]
print(''.join(res_decode))


# In[ ]:


a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))


# In[ ]:


def code(source, end, data):
    ''' Data coder '''
    cryptData = ''
    for char in data:
        cryptData += end[source.index(char)]
    return cryptData

# Input data
key1 = input()
key2 = input()
decode = input()
encode = input()

print(code(key1, key2, decode))
print(code(key2, key1, encode))


# In[ ]:


a= int(input())
b=[]
for i in range(a):
    x=input().lower()
    if x not in b:
        b.append(x)
d=int(input())
e=[]
for j in range(d):
    x=input().lower().split()
    for i in x:
        if i not in b and i not in e:
            e.append(i)
print('\n'.join(e))


# In[ ]:


count_dict = int(input())
dict = []
check_words = []
result = []

#заполняем словарь
for i in range(count_dict):
  dict.append(input().lower())


count_lines = int(input())

#заполняем список проверяемых слов
for i in range(count_lines):
  check_words += input().lower().strip().split(' ')


#выбираем слова которые не проходят проверку
for i in check_words:
  if i not in dict and i not in result:
    result.append(i)


#печатаем
for i in result:
  print(i)


# In[ ]:


word_count=int(input())
d=[]
check_words=[]
result=[]
for i in range(word_count):
    d.append(input().lower())
count_lines=int(input())
for i in range(count_lines):
    check_words+=input().lower().strip().split(' ')
for i in check_words:
    if i not in d and i not in result:
        result.append(i)
for i in result:
    print(i)


# In[ ]:





# In[ ]:


napr = {'север': (0, 1), 'запад': (-1, 0), 'юг': (0, -1), 'восток': (1, 0)}
n = int(input('Vvedite chislo n: '))
x_list = [(input('napravlenie i sm. cherez probel: ')).split(' ') for x in range(n)]
dvizh = [(napr[x][0]*int(y), napr[x][1]*int(y)) for x, y  in x_list]
res = (sum([x for x, y in dvizh]), sum([y for x, y in dvizh]))
print(' '.join(map(str, res)))


# In[8]:


with open('d:\Basic\dataset_3380_5.txt') as inf:
    p=[]
    d={}
    for line in inf:
        p.append(line.strip('\n').split('\t'))
    #print(p)
    for y in p:
        y[0]=int(y[0])
        y[2]=int(y[2])
    #print(p)
    for c in p:
        if int(c[0]) in d:
            d[c[0]].append(c[2])
        else:
            d[c[0]]=[c[2]]
    #print(d)
    for k in sorted(d.keys()):
        print(k, '',sum(d[k])/float(len(d[k])))


# In[12]:


with open('d:\Basic\dataset_3380_5.txt') as inf:
    p=[]
    d={}
    for line in inf:
        p.append(line.strip('\n').split('\t'))
    for i in p:
        i[0]=int(i[0])
        i[2]=int(i[2])
    for t in p:
        if int(t[0]) in d:
            d[t[0]].append(t[2])
        else:
            d[t[0]]=[t[2]]
    for j in sorted(d.keys()):
        print(j, '',sum(d[j])/float(len(d[j])))


# In[ ]:


height = {i:[] for i in range(1,12)}
def reading(file_name):
	with open(file_name) as f:
		for line in f.readlines():
			cl, _, growth = line.split()
			cl, growth = int(cl), int(growth)
			height[cl].append(growth)

def average():
	for cl in height:
		if height[cl]:
			height[cl] = sum([h for h in height[cl]])/len(height[cl])
		else:
			height[cl] = '-'
def display():
	for cl, growth in sorted(height.items()):
		print(cl, growth)

reading('d:\Basic\dataset_3380_5.txt')
average()
display()


# In[ ]:


d = dict()
with open('d:\Basic\dataset_3380_5.txt') as inf:
    for line in inf:
        a, b, c = line.strip().split( )
        d.setdefault(a, []).append(int(c))

k = 1 

while k <= 11:
    if str(k) in d.keys():
        print(k, sum(d.get(str(k)))/len(d.get(str(k))))
    else:
        print(k, '-')
    k += 1


# In[ ]:


classes = {i: [] for i in range(1, 12)}
with open('d:\Basic\dataset_3380_5.txt') as f:
    for line in f:
        cls, name, height = line.strip().split('\t')
        classes[int(cls)].append(int(height))

for cls, heights in classes.items():
    print(cls, sum(heights) / len(heights) if heights else '-')


# In[ ]:


d = {i:[0, 0] for i in range(1, 12)}
with open('d:\Basic\dataset_3380_5.txt') as a:
    for i in a:
        s = i.split('\t')
        sum_height = d[int(s[0])][0] + int(s[2])
        n = d[int(s[0])][1] + 1
        d[int(s[0])] = [sum_height, n]
for i in d:
    if d[i][1] == 0:
        print(i, '-')
    else:
        print(i, d[i][0]/d[i][1])


# In[ ]:


import pandas as pd

df = pd.read_table('d:\Basic\dataset_3380_5.txt', header=None, sep=r'\s{1,}')
print(df.groupby(0).mean())


# In[ ]:




