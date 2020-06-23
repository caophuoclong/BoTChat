import speech_recognition as sp
import brain
import time
import os
import botsay
import install
install.main()
losa = sp.Recognizer()
while True:
    time.sleep(0.1)
    with sp.Microphone() as source:
        audio = losa.listen(source,phrase_time_limit=10)
    
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
        botsay.main(bot)
        if bot == "Máy sẽ tắt trong 1 phút" :
            botsay.main("Bạn có thể ngưng việc tắt máy bằng cách nhập vào terminal shutdown -c")
            print("Bạn có thể ngưng việc tắt máy bằng cách nhập vào terminal shutdown -c")
            os.system("shutdown +1 ")
