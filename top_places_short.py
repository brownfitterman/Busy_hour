import requests as re
import json

data=re.get("https://www.postman.com/collections/89680f8c550554cdcfb4")
googlePlaceName=[]
data1=(data.json())["item"][0]["request"]["body"]["raw"]
data1=json.loads(data1)
for i in data1:
    place_name=i["googlePlaceName"]
    googlePlaceName.append(place_name)
    print(googlePlaceName)
    

    
        

