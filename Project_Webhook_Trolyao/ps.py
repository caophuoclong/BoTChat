import speech_recognition as sp
import brain
import time
import os
import botsay
losa = sp.Recognizer()
while True:
    time.sleep(0.1)
    print("Listening...")
    with sp.Microphone() as source:
        audio = losa.listen(source,phrase_time_limit=5)
    
    try:
        x  = losa.recognize_google(audio,language="vi-VN")
    except:
        x = ""
        time.sleep(0.1)
    if "bye" in x or "tạm biệt" in x:
        print("You said: " + x)
        print("Bot...")
        time.sleep(1)
        print("Bot said: Tạm biệt")
        botsay.main("Tạm biệt")
        break
    elif x == "":
        time.sleep(0.1)
        continue
    else:
        bot = brain.proccess(x)
        print("You said: " + x)
        print("Bot...")
        time.sleep(1)
        print("Bot said: " + bot)
        if bot == "Máy sẽ tắt trong 1 phút" :
            botsay.main("Bạn có thể ngưng việc tắt máy bằng cách nhập vào terminal shutdown -c")
            print("Bạn có thể ngưng việc tắt máy bằng cách nhập vào terminal shutdown -c")
            os.system("shutdown +1 ")
        elif bot == "shutdown now":
            os.system("shutdown now")
        elif "drive" in bot.lower():
            os.system("google-chrome drive.google.com")
        elif "google" in bot.lower():
            botsay.main("Đang mở google chrome")
            time.sleep(0.75)
            os.system("google-chrome")
        elif "code" in bot.lower():
            botsay.main("Đang vở visual Code")
            time.sleep(0.75)
            os.system("code")
        elif "youtube" in bot.lower():
            botsay.main("Đang mở youtube")
            time.sleep(0.75)
            os.system("google-chrome youtube.com")
        elif "reboot" in bot.lower():
            os.system("reboot")
        elif bot.lower() == "ngưng tắt máy":
            os.system("shutdown -c")
        elif "facebook" in bot.lower():
            os.system("google-chrome facebook.com")
        elif "gmail" in bot.lower():
            os.system("google-chrome gmail.com")
        elif "file" in bot.lower() or "phai" in bot.lower():
            os.system("dolphin")
        elif bot.lower() == "...":
            continue
        else:
            botsay.main(bot)
