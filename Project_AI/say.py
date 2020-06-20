import pyttsx3
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific

# Use female English voice
engine.setProperty('rate', 130)    # Speed percent (can go over 100)
engine.setProperty('voice', "vietnam")
#engine.say("Hello my friend")
engine.say('xin chào bạn của tôi')

engine.runAndWait()