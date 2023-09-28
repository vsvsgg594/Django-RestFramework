import requests
import json


URL="http://127.0.0.1:8000/h"
def get_data(id=None):
    data={}

    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)

    r=requests.get(url =URL,data=json_data)

    print(data)

# get_data()


def post_data():
    data={'name':'vikash',
        'roll':123,
        'city':'Bihar'}
    headers={'context-Type':'application/json'}
    
    json_data=json.dumps(data)

    r=requests.post(url=URL,headers=headers,data=json_data)

    data=r.json()

    print(data)

post_data()    