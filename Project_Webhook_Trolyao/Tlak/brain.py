import datetime
import time
import pytz
import sisimi
def proccess(stri):
    thu = {"Sunday" : "Chủ nhật", "Saturday" : "Thứ 7", "Friday": "Thứ 6", "Thursday" : "Thứ 5","Wednesday" :"Thứ 4","Tuesday":"Thứ 3","Monday":"Thứ hai"}
    x = "" + stri
    if "thứ" in x.lower() and "hôm nay" in x.lower():
        return thu[datetime.datetime.now().strftime("%A")]
    elif "today" in x.lower() or "hôm nay" in x.lower():
       return datetime.datetime.now().strftime("%d-%m-%Y")
    elif "time" in x.lower() or "giờ" in x.lower():
        return datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("%H giờ %M phút %S giây")
    elif "name" in x.lower() or "tên" in x.lower():
        return "Mình là con bot đẹp trai nè"
    elif "tổng thống" in x.lower():
        return "Donal Trump"
    elif "chào" in x.lower():
        return "Chào bạn"
    elif "tắt máy" in x.lower() or "shutdown" in x.lower() or "shut down" in x.lower():
        return "Máy sẽ tắt trong 1 phút"
    else:
        return sisimi.main(x)