import requests
import json

def Not_Need_text(text):
    try:
        if text in "richText":
            return False
        elif text in "종류":
            return False
        else:
            return True
    except:
        return False
data = requests.get("http://10.150.150.50:3000/food").json()

a=0
for item in data:
    if Not_Need_text(item[1]):
        print(a,item[1])
        a+=1