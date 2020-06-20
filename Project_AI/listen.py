import speech_recognition

say = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("Say some thing: ")
    audio = say.listen(mic)

try:
    sx = say.recognize_google(audio)
except:
    sx = ""

print(sx)
