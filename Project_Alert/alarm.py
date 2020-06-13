import time
import notify2
import os
import pytz
import datetime

def gettime(x):
    whattime = time.time()
    notify2.init("Python")
    if x < whattime:
        alarm()
    while whattime < x:
        whattime = time.time()
    n = notify2.Notification("Alarm","Timeeeeee")
    n.show()
    print(whattime)
def alarm():
    timsa = input("Thoi gian bao thuc: ")
    future = datetime.datetime.date(datetime.datetime.now()).strftime("%d-%m-%y ") + timsa
    timestam = datetime.datetime.timestamp(datetime.datetime.strptime(future,"%d-%m-%y %H:%M"))
    return timestam


if __name__ == "__main__":
    gettime(alarm())
