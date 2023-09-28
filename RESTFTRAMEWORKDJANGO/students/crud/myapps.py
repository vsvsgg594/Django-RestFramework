import io
import json
import requests
URL=""

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    jnso_data=json.dumps(data)



    r=requests.get(url=URL,data=jnso_data)

    data=r.json()


    print(data)

get_data(1)

