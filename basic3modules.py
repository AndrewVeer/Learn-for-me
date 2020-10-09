import requests

with open('d:\Basic\dataset_3378_2.txt') as inf:
    url=inf.read().strip()

r=requests.get(url)
c=0

for line in r.requests.splitlines():
    c+=1

with open('d:\Basic\out.txt','w') as ouf:
    ouf.write(str(c))