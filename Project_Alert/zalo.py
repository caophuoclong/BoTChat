import requests
import json
def xincq():
    url = "https://oauth.zaloapp.com/v3/permission?"
    param={
        "app_id" : "3925863727448935908",
        "redirect_uri" : "https://b8c84554c8d2446ebbf2a14ab67556f2.m.pipedream.net/",
        "state" : "Longdeeptry"
    }
    x = requests.request("GET",url,params=param)
    print(x.text)

def print1():
    url = "https://48688f2f8529a2d2fd2630be335733d6.m.pipedream.net"
    x = requests.post(url)
    print(x.text)
xincq()