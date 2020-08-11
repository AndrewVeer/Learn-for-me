#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))**0.5
print(S)


# In[10]:


a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print (s)
else:
    print ('Не выполнено неравенство треугольника')


# In[18]:


a=int(input())
if -15<a<=12 or 14<a<17 or 19<=a:
    print('True')
else:
    print('False')


# In[20]:


a=int(input())
print(-15<a<=12 or 14<a<17 or 19<=a)


# In[45]:


a=float(input())
b=float(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/' and b!=0:
    print(a/b)
elif c=='*':
    print(a*b)
elif c=='mod' and b!=0:
    print(a%b)
elif c=='pow':
    print(a**b)
elif c=='div' and b!=0:
    print(a//b)
else:
    print('Деление на 0!')


# In[48]:


a, b = float(input()), float(input())
print({'+':   a + b,
       '-':   a - b,
       '*':   a * b,
       '/':   a / b if b != 0 else "Деление на 0!",
       'mod': a % b if b != 0 else "Деление на 0!",
       'pow': a ** b,
       'div': a // b if b != 0 else "Деление на 0!"}[input()])


# In[54]:


d=input()
if d=='треугольник':
    a=int(input())
    b=int(input())
    c=int(input())
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        s=float((p*(p-a)*(p-b)*(p-c))**0.5)
        print (s)
    else:
        print ('Не выполнено неравенство треугольника')
if d=='круг':
    r=int(input())
    n=3.14
    S=float(n*(r**2))
    print(S)
if d=='прямоугольник':
    a=int(input())
    b=int(input())
    S=float(a*b)
    print(S)


# In[56]:


shape = input()
if (shape == 'круг'):
    print(float(3.14*int(input())**2))
elif (shape == 'прямоугольник'):
    print(float(int(input())*int(input())))
elif (shape == 'треугольник'):
    a,b,c = int(input()),int(input()),int(input())
    p = (a + b + c)/2
    print(float((p * (p - a) * (p - b) * (p - c))**0.5))


# In[127]:


A,B,H=int(input()),int(input()),int(input())
a,b,c=str,str,str=A,B,H
if b>a:
    if c<b:
        if c<a:
            if a<b>c:
                print(b,c,a,sep='\n')
        else:
            print(b,a,c,sep='\n')            
    else:
        print(c,a,b,sep='\n')
if a>=b:
    if c>=b:
        if c>=a:
            if a<=c>=b:
                print(c,b,a,sep='\n')
        else:
            print(a,b,c,sep='\n')
    else:
        print(a,c,b,sep='\n')


# In[68]:


a=8
b=2
c=14
result=a if a>b else b
result1=c,b,a if (a<c>b) else a,b,c
print(result1)


# In[215]:


a,b,c=int(input()),int(input()),int(input())
if (b>a and c<=b and c<=a and a<b>c): print(b,c,a,sep='\n')
elif (b>a and c<=b and c>=a): print(b,a,c,sep='\n')            
elif (b>a and c>=b): print(c,a,b,sep='\n')
if (a>=b and c>=b and c>=a and a<c>b): print(c,b,a,sep='\n')
elif (a>=b and c>=b and c<=a): print(a,b,c,sep='\n')
elif (a>=b and c<=b): print(a,c,b,sep='\n')


# In[195]:


a,b,c = int(input()), int(input()), int(input())
if a < b: a, b = b, a
if a < c: a, c = c, a
if b > c: b, c = c, b
print(a,b,c,sep='\n')


# In[203]:


a, b, c = int(input()), int(input()), int(input())
print((max(a, c, b)),(min(a, c, b)),(a + b + c - max(a, b, c) - min(a, b, c)),sep='\n')


# In[217]:


a,b,c = int(input()),int(input()),int(input())
if a>=b>=c : print(a,c,b,sep='\n')
elif a>=c>=b: print(a,b,c,sep='\n')
elif b>=a>=c: print(b,c,a,sep='\n')
elif b>=c>=a: print(b,a,c,sep='\n')
elif c>=a>=b: print(c,b,a,sep='\n')
else: print(c,a,b,sep='\n')


# In[241]:


a=int(input())
x,y,z='программист','программиста','программистов'
if a%10==1 and a%100!=11: print(a,x)
elif a%10>=2 and a%10<=4 and (a%100<10 or a%100>20): print(a,y)
else: print(a,z)


# In[286]:


a=int(input())
b=int(a/100000)
c=int((float(a/100000)-b)*10)
d=int((float(a/10000)-int(a/10000))*10)
e=int((float(a/1000)-int(a/1000))*10)
f=int((float(a/100)-int(a/100))*10)
g=int((float(a/10)-int(a/10))*10)
print(b,c,d,e,f,g,sep='\n')
#s1=b+c+d
#s2=e+f+g
#if s1==s2: print('Счастливый')
#else: print('Обычный')


# In[42]:


a=int(input())
b=a//100000
c=((a//10000)-((a//100000)*10))
d=((a//1000)-((a//10000)*10))
e=((a//100)-((a//1000)*10))
f=((a//10)-((a//100)*10))
g=a%10
s1=float(b+c+d)
s2=float(e+f+g)
if s1==s2: print('Счастливый')
else: print('Обычный')


# In[44]:


a=(input()
a1=a%10
a2=(a%100)//10
a3=(a%1000)//100
a4=(a%10000)//1000
a5=(a%100000)//10000
a6=a//100000
if a1+a2+a3==a4+a5+a6:
    print('Счастливый')
else:
    print('Обычный')


# In[45]:


a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')


# In[47]:


x = int(input())
a = x // 1000
b = x % 1000
if a // 100 + a % 100 // 10 + a % 10 == b // 100 + b % 100 // 10 + b % 10:
    print('Счастливый')
else:
    print('Обычный')


# In[ ]:


a, b, c, d, e, f = input()
print ('Счастливый' if int(a)+int(b)+int(c)==int(d)+int(e)+int(f) else 'Обычный')


# In[ ]:




