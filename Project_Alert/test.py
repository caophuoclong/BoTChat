import requests

url = "https://centralus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

re = requests.post(url)

print(re.text)