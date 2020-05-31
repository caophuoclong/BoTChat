import requests
import json
import time
import os
import aiml
import weather


def convert(messe):
    savefile = os.getcwd()
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
    page = requests.get(link)
    while page.status_code == 404:
        page = requests.get(link)
    fname = "Play"+str(int(time.time()))+".wav"
    filelo = "{}/{}".format(savefile,fname)
    file = open(filelo.format(fname), 'wb')
    
    file.write(page.content)
    file.close()
    

    file = filelo
    os.system("mpg123 " + file)
    os.remove(filelo)
def text(x):
    return x

def main(ms):
    kernel = aiml.Kernel()
    kernel.learn("start.xml")
    kernel.respond("load aiml b")
    file = open("history.txt","w+")
    x = "Long"
    while x != "q":
        x = ms
        if x == "q":
            break
        if x == None:
            x = "q"
            messe = kernel.respond(x)
            file.write(messe)
            file.close
            convert(messe)
            
        if x == "/w":
            wea = weather.main()
            convert(wea)
        else:
            messe = kernel.respond(x)
            file.write(messe)
            file.close
            convert(messe)
            return messe
        break
