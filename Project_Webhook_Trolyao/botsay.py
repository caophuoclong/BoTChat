import datetime
from gtts import gTTS
from playsound import playsound
import os
def main(x):
    v =gTTS(text=x,lang="vi",slow=False)
    name = datetime.datetime.now().timestamp()
    filepath = "/home/phuoclong/Project/Sound/{}".format(str(int(name)) + ".mp3")
    v.save(filepath)
    playsound(filepath)
    