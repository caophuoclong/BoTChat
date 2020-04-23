import requests
import json
import datetime
import pytz
    

def GetDataVN():
    x = "Vietnam"
    er = pytz.timezone("Asia/Ho_Chi_Minh")
    dte1 = datetime.datetime.now(er)
    s1 = dte1.strftime("Ngày %d/%m/%Y - %H:%M:%S")
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"format":"json","name":"{}".format(x)}

    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "4bd85a6a07msh7f74b759e98a61cp1db7efjsnf7ce5fdb6b89"
    }
    a = json.loads(requests.get(url,headers=headers,params=querystring).text)
    b = a[0]
    time = "{}".format(s1)
    country = "\nQuốc Gia: " + b.get("country")
    case1 = "\nSố ca nhiễm bệnh: " + str(b.get("confirmed"))
    case2 = "\nSố ca tử vong: " + str(b.get("deaths"))
    case3 = "\nSố ca hồi phục: " + str(b.get("recovered"))
    total = time + country + case1 + case2 + case3 
    return total

def GetDataWorld():
    url = "https://covid-19-data.p.rapidapi.com/totals"
    querystring = {"format":"json"}
    er = pytz.timezone("Asia/Ho_Chi_Minh")
    dte1 = datetime.datetime.now(er)
    s1 = dte1.strftime("Ngày %d/%m/%Y - %H:%M:%S")
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "4bd85a6a07msh7f74b759e98a61cp1db7efjsnf7ce5fdb6b89"
        }

    a = json.loads(requests.get(url,headers=headers,params=querystring).text)
    b = a[0]
    time = "{}".format(s1)
    country = "\nThế giới" 
    case1 = "\nSố ca nhiễm bệnh: " + str(b.get("confirmed"))
    case2 = "\nSố ca tử vong: " + str(b.get("deaths"))
    case3 = "\nSố ca hồi phục: " + str(b.get("recovered"))
    total = time + country + case1 + case2 + case3
    return total
    
def main(): 
    title = "Cập Nhập Số liệu COVID-19"
    total1 = title + "\n\n\n" + GetDataWorld() + "\n\n\n" + GetDataVN()
    return total1

