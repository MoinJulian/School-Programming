import requests

URL = "http://172.19.2.131:5173/api/test"
r = requests.get(url = URL)
data = r.json()
print(data)
