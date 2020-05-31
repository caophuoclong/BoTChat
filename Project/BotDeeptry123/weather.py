import requests
import json
import datetime
def main():
    url = "http://api.openweathermap.org/data/2.5/weather?id=1586203&appid=031a8e22affaa43ce09c0a84a8b3f29c"
    
    start = datetime.datetime.fromtimestamp(1586099614)
          
    re = requests.request("GET",url)
    re = re.json()
    lon = "\nKinh độ: "+str(re["coord"].get("lon")) #: 
    lat = "\nVĩ độ: "+str(re["coord"].get("lat")) #: 
    wea = "\nThời tiết: "+re["weather"][0].get("main") #: 
    
    temp = "\nNhiệt độ: " + str(round((re["main"].get("temp")+re["main"].get("feels_like"))/2-273.15,2)) + " C" #Nhiet do K -> C
    pre = "\nÁp suất: "+str(round(re["main"].get("pressure")*(9.87*(1/10000)),2)) + " atm" #Ap suat
    humi = "\nĐộ ẩm: "+str(re["main"].get("humidity"))+"%" #Do am %
    wins="\nTốc độ gió: "+str(re["wind"].get("speed")*3.6)+" km/h" #toc do gio m/s
    giodo = "\nĐo vào lúc: "+ str(datetime.datetime.fromtimestamp(re["dt"],re["sys"].get("timezone"))) #gio do
    binhminh = "\nBình minh: "+ str(datetime.datetime.fromtimestamp(re["sys"].get("sunrise"),re["sys"].get("timezone"))) #Binh minh
    hoanghon = "\nHoàng hôn: " + str(datetime.datetime.fromtimestamp(re["sys"].get("sunset"),re["sys"].get("timezone"))) #Hoang hon
    noido = "\nVị trí: " +re["name"] #noi do
    total = noido + giodo + temp + humi + pre + wins + wea + lon + lat + binhminh + hoanghon
    return total





