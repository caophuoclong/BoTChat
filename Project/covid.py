import requests
import json
def main(x):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":x}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "9e27549a4cmsh0589e1006cbae50p151d08jsnc050a6748ebf"
        }

    response1 = requests.request("GET", url, headers=headers, params=querystring)
    a = json.loads(requests.get(url,headers=headers,params=querystring).text)
    data = a["data"].get("lastChecked")
 
    data1 = a["data"].get("covid19Stats")
    
    count = 0
    count1 = 0
    count2 = 0
    for i in range(len(data1)):
        count = data1[i].get("confirmed")
        count1 = data1[i].get("deaths")
        count2 = data1[i].get("recovered")

    update = "Update lần cuối: " + data
    country = "\nQuốc Gia: " + data1[0].get("country")
    case1 = "\nSố ca nhiễm bệnh: " + str(count)
    case2 = "\nSố ca tử vong: " + str(count1)
    case3 = "\nSố ca hồi phục: " + str(count2)
    soure = "\nNguồn: https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics/endpoints"
    total = update + country + case1 + case2 + case3 + soure
    return total
