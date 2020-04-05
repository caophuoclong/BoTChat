import requests
import json
import urllib.request
def main():
    url = "https://aws.random.cat/meow"

    a = requests.request("GET",url)
    e = json.loads(requests.request("GET",url).text)
    b = e.get("file")
    return b
    



        


 
