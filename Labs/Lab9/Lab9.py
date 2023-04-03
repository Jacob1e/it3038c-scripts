import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()

count = 0
while (count < 4):
    print(data[count]['name'] + ' is ' + data[count]['color'])
    count = count + 1
