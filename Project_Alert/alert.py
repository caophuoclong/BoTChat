import datetime
import pytz 
import notify2
import os
import time
def main():
    os.system("clear")
    fileDrink = "/home/phuoclong/Sound/drink.mp3"
    fileStand = "/home/phuoclong/Sound/stand.mp3"
    now = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).timestamp()
    print(datetime.datetime.fromtimestamp(now).strftime("{}: %H:%M:%S".format("Hiện tại")))
    future = now + 30    * 60
    print(datetime.datetime.fromtimestamp(future).strftime("{}: %H:%M:%S".format("Tương lai")))
    while now < future:
        now = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).timestamp()
        print(datetime.datetime.fromtimestamp(now).strftime("%H:%M:%S"))
        if now > (future - (19 * 60)) and now < (future - ((20 * 60) - 30)):
            for i in range(3):
                notify2.init('Standing')
                n = notify2.Notification("Đứng dậy đi")
                n.show()
                os.system("mpg123 "+ fileStand)
        time.sleep(1);
    else:
        for i in range(3):
            notify2.init('Drinking water')
            n = notify2.Notification("Hãy đi uống nước...")
            n.show()
            os.system("mpg123 " + fileDrink)
    time.sleep(3)   
    main()



if __name__ == "__main__":
    main()            