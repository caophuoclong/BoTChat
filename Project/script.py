import requests
import json
from urllib.request import urlopen
import time
import os
import aiml

def convert(messe):
    savefile = "/home/phuoclong/Speech"
    url = 'https://api.fpt.ai/hmi/tts/v5'

    payload = messe
    headers = {
        'api-key': '01Z9YWzOvYWRMJgiy2VBAomzMvLpeU3F',
        'speed': '-1',
        'voice': 'banmai'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    x = json.loads(response.text)
    link = x.get('async')
    rqus = requests.get(link)
    print("Long")
    page = requests.get(link)
    while page.status_code == 404:
        page = requests.get(link)
    fname = "Play"+str(int(time.time()))+".wav"
    filelo = "{}/{}".format(savefile,fname)
    file = open(filelo.format(fname), 'wb')
    
    file.write(page.content)
    file.close()
    import os

    file = filelo
    os.system("mpg123 " + file)
    os.remove(filelo)

def main():
    kernel = aiml.Kernel()
    kernel.learn("start.xml")
    kernel.respond("load aiml b")
    convert("Xin chào bạn")
    x = "Long"
    while x != "q":
        x = input("Nhap du lieu: ")
        if x == "q":
            break
        if x == None:
            x = "q"
        messe = kernel.respond(x)
        convert(messe)

if __name__ == "__main__":
    main()