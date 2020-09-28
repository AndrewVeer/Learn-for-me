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


# In[42]:


with open('d:\Basic\dataset_3363_2.txt','r') as inf:
    a=inf.readline()
b = []
d=''
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
for i in range(len(b)):
    d+=(b[i]*int(c[i]))
    print(b[i]*int(c[i]),end="")
with open('d:\Basic\output.txt','w') as ouf:
    ouf.write(d)


# In[ ]:





# In[33]:


with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j


# In[ ]:


m, s, n = '', '', 0
with open('dataset_3363_2.txt', 'r+') as f:     # открываем файл в режиме чтение и запись
    for i in f.readline():                      # читаем строку и перебираем
        if '0' <= i <= '9':                     # если число
            n += i                              # соединяем числа в строку
            continue
        m += s * int(n)                         # преобразуем число в соответствующее количество символов
        s, n = i, ''
    f.seek(0)                                   # перемещаем указатель в начало файла для перезаписи
    f.write(m)                                  # записываем преобразованную строку в файл


# In[56]:


result,bukva,chislo='','',0
with open('d:\Basic\dataset_3363_2.txt','r') as inf:
    a=inf.readline()
for i in a:
    if '0'<=i<='9':
        chislo+=i
        continue
    result+=bukva*int(chislo)
    bukva,chislo=i,''
with open('d:\Basic\exit.txt','w') as ouf:
    ouf.write(result)


# In[ ]:


import re                         ﻿#подгрузил библиотеку с регулярными выражениями, рекомендую прочитать статью 
                                  ﻿#https://tproger.ru/translations/regular-expression-python/﻿
vyvod=''                          ﻿#объявил пустую строку в которую в конце буду все записывать
with open("dataset_3363_2.txt") as file:   #открываю файл
  line = file.readline().strip()           #читаю строку
bukvi = re.findall(r'\D', line)            #re.findall находит все сочетания до цифры и помещает их в список 
                                           #в виде ('a', 'A', 'c'...) ﻿﻿ 
                                           #\﻿d - ﻿Любая цифра [0-9] (\D — все, кроме цифры)﻿﻿ ﻿
cifri = re.findall(r'\d+', line)           #\d ﻿﻿находит все сочетания цифр, а остальные пропускает, но чтобы он не
                                           #оставлял пробелы вместо пропущенных букв написано '\d+' - где + 
﻿                                          ﻿ #обозначает 1 и ﻿более вхождений цифр (по умолчанию, как я понял 0 и
                                           #более вхождений)﻿  
﻿for i in range(len(bukvi)):               #поскольку букв и сочетаний цифр одинаковое количество, то цикл
                                           #﻿имеет ﻿одинаковую длину (len(bukvi)) как для цифр, так и для букв   
    vyvod+= str(bukvi[i])*int(cifri[i])    #каждую букву записываю в ﻿строку определенное количество раз
with open("textfile_out.txt", "w") as outfile: outfile.write(vyvod) #записываю в файл


# In[ ]:





# In[ ]:





# In[71]:


dictionary = {}

with open('d:\Basic\dataset_3363_3.txt') as in_f_obj:
	for line in in_f_obj:
		line = line.lower()
		for word in line.split():
			if word not in dictionary:
				dictionary[word] = 1
			elif word in dictionary:
				dictionary[word] += 1			

max_quantity = 1
	
for key, value in dictionary.items():
	current_quantity = dictionary[key]
	if current_quantity > max_quantity:
		max_quantity = current_quantity
		word_with_max_quantity = key
	
with open('d:\Basic\output3.txt', 'w') as out_f_obj:
	most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
	out_f_obj.write(most_popular)


# In[ ]:


with open('d:\Basic\dataset_3363_3.txt') as inf, open('d:\Basic\MostPopularWord.txt','w') as ouf:
    maxc=0
    s=inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter=s.count(word)
        if counter>maxc:
            maxc=counter
            resultword=word
        ouf.write(resultword+' '+str(maxc))


# In[30]:


s,sred,fst,snd,trd=[],[],[],[],[]
with open ('d:\Basic\dataset_3363_4.txt','r') as inf:
    for line in inf:
        s.append(line.strip().split(';'))

for i in s:
    sred.append((int(i[1])+int(i[2])+int(i[3]))/3)
    fst.append(int(i[1]))
    snd.append(int(i[2]))
    trd.append(int(i[3]))
f=open('d:\Basic\exit1.txt', 'w+')
for i in sred:
    print(i,file=f)
print((sum(fst)/len(fst)),(sum(snd)/len(snd)),(sum(trd)/len(trd)),file=f)


# In[ ]:


# Для тех, кто хочет сократить свой код :) написал небольшое руководство по [list comprehension]
# на основе примера на stackoverflow.com
# # http://stackoverflow.com/questions/16632124/python-emulate-sum-using-list-comprehension
# я немного изменил этот пример, чтобы лучше объяснить работу [list comprehension]
# и вам было проще понять, как применить этот подход к решению задания

# допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
# т.е. по сути это список списков :)
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
# представьте, что наш список списков - это таблица из трёх столбцов
# и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
# в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

# поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
# ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
# вы можете сделать это примерно так
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# надеюсь, вам было понятно и интересно
# желаю успехов в учёбе!!!


# In[25]:





# In[ ]:





# In[ ]:





# In[ ]:


import pandas as pd

df = pd.read_csv('dataset_3363_4.txt', sep=';', names=['Фамилия','Математика', 'Физика', 'Русский язык'])
mat = df['Математика'].mean()

phis = df['Физика'].mean()

rus = df['Русский язык'].mean()

df['Среднее ученика'] = (df['Математика'] + df['Физика'] + df['Русский язык']) / 3

mean_learn = df['Среднее ученика']

with open('result.txt', 'w') as file:
    for value in mean_learn:
        file.write(str(value)+'\n')
    file.write(str(mat)+' '+str(phis)+' '+str(rus))


# In[50]:





# In[34]:


koll,p,v,t=0,0,0,0
with open('d:\Basic\dataset_3363_4.txt','r')as inf:
    for line in inf:
        line=line.strip().split(';')
        fst,snd,trd=int(line[1]),int(line[2]),int(line[3])
        print((fst+snd+trd/3))
        koll+=1
        p+=fst
        v+=snd
        t+=trd
with open('d:\Basic\output1.txt','w') as ouf:
    ouf.write(str(p/koll))
    ouf.write(str(v/koll))
    ouf.write(str(t/koll))


# In[ ]:




