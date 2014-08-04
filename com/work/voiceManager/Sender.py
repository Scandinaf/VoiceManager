import requests

recording = 'C:/Users/sborovskiy/PycharmProjects/VoiceManager/com/work/voiceManager/output.flac'
url = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=ru-RU'
headers = {'Content-Type' : 'audio/x-flac; rate=16000', 'User-Agent': 'Netscape 6.0'}
files = {'output.flac' : open(recording, 'rb')}
response = requests.post(url = url, data = files, headers = headers)
