import requests
import json
import random
class x():

    def main(self): 
        i = random.randint(0,250)
        url = "https://restcountries.eu/rest/v2/all"

        re = requests.request("GET",url)

        a = re.json()
        
        country = "Quốc Gia: " + a[i]["name"]
        capital = "\nThủ đô: " + a[i]["capital"]
        population = "\nDân số: " + str(a[i]["population"])
        area = "\nDiện tích: " + str(a[i]["area"])
        region = "\nChâu lục: " + a[i]["region"]
        khuvuc = "\nKhu vực: " + a[i]["subregion"]
        borders = "\nTiếp giáp: "
        for j in a[i]["borders"]:
            borders += j + ", "
        latlng ="\nTọa độ: "
        for j in a[i]["latlng"]:
            latlng += str(j) +  ", "
        timezones = "\nMúi giờ: "
        for j in a[i]["timezones"]:
            timezones += j +", "
        total = country + capital + population + area + region + khuvuc
        total = total + borders + latlng + timezones
        return total
  
        
        