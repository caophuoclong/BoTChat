import requests

url = "http://api.simsimi.com/request.p"

querystring = {"ft":"0.0","text":"xin chao","lc":"en"}

headers = {
    
    'x-api-key': "4G-55qefmZh0QlkAkfQjSaDuQJMcaTHktmP3NeTU"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)