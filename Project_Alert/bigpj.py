import requests
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
import os
import azure.cognitiveservices.speech as speechsdk #Thu vien chuyen sound file sang text file
class Bot:
    def record1():
        fs = 44100  # this is the frequency sampling; also: 4999, 64000
        seconds = 5  # Duration of recording
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        print("Starting: Speak now!")
        sd.wait()  # Wait until recording is finished
        print("finished")
        write('output.wav', fs, myrecording)  # Save as WAV file
    
    def speechtotext(record1):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
        #url = "https://centralus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"
        
        speech_key, service_region = "ac751e8f-0a25-4430-918e-e3d3703a2c41", "centralus"
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

        # Creates an audio configuration that points to an audio file.
        # Replace with your own audio filename.
        audio_filename = "/home/phuoclong/Project/output.wav"
        audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

        # Creates a recognizer with the given settings
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

        print("Recognizing first result...")

        # Starts speech recognition, and returns after a single utterance is recognized. The end of a
        # single utterance is determined by listening for silence at the end or until a maximum of 15
        # seconds of audio is processed.  The task returns the recognition text as result. 
        # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
        # shot recognition like command or query. 
        # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
        result = speech_recognizer.recognize_once()

        # Checks result.
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    def texttospeech():
        pass
    def process():
        pass
    def alert():
        pass
    def search():
        pass

if __name__ == "__main__":
    bot =Bot
    #bot.record()
    bot.speechtotext(bot.record1())