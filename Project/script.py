import requests
import json
import time
import os
import aiml
import weather
import test


def convert(messe):
    savefile = os.getcwd() #Lấy địa chỉ lưu file
    url = 'https://api.fpt.ai/hmi/tts/v5' 

    payload = messe
    headers = {
        'api-key': '01Z9YWzOvYWRMJgiy2VBAomzMvLpeU3F',
        'speed': '-1',
        'voice': 'banmai'
    }
    print("Long1")
    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    x = json.loads(response.text)
    link = x.get('async') # Lấy link của file mp3
    print(link)
    page = requests.get(link) # Gửi request.
    while page.status_code == 404: # Check xem request có lỗi không
        page = requests.get(link)
    print("Long2") 
    fname = "Play"+str(int(time.time()))+".wav" #Tạo tên file.
    filelo = "{}/{}".format(savefile,fname) #Đường dẫn tới file mp3
    file = open(filelo.format(fname), 'wb') #Mở file theo dạng nhị phân
    
    file.write(page.content) #Ghi file nhị phân.
    file.close()
    

    file = filelo
    print("Long3")
    os.system("mpg123 " + file) #Dùng package mpg123 để chạy file mp3
    print("Long4")
    os.remove(filelo) #Xóa file sau khi dùng xong
def text(x):
    return x

def main(ms):
    file = open("history.txt","w+")
    x = "Long"
    while x != "q":
        x = input("Type Some thing: ")
        if x == "q":
            break
        if x == None:
            x = "q"
            messe = test.simsimi(x)
            file.write(messe)
            file.close
            convert(messe)
            
        if x == "/w":
            wea = weather.main() # Đọc thời tiết tại vị trí cần thơ
            convert(wea)
        else:
            messe = test.simsimi("Xin chao ban")
            print(messe)
            file.write(messe)
            file.close
            convert(messe)
            return messe
        break
main("Long")
