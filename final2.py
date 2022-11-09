import requests
import random

x=random.randint(-90,90)
y=random.randint(1,360)

url ="http://10.12.101.32:5000" 
code=(x,y)
params = {'location' : code}
r= requests.get(url=url,params=params)
response=requests.get(url=url,data=params)
print(response)


