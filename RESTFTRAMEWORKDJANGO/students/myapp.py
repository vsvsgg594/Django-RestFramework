import requests
import json

URL="http://127.0.0.1:8000/stdcreate/"

data={
    'name':'r',
    'roll':123431,
    'city':'patna'
}

jsno_data=json.dumps(data)
r=requests.post(url=URL,data=jsno_data)
data1=r.json()
print(data1)