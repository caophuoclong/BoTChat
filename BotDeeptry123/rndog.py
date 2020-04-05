import requests
import json
def main():
    url = "https://random.dog/woof.json"

    re = requests.request("GET",url)
    a = re.json()
    a = a["url"]
    return a