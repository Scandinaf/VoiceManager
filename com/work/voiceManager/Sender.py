import urllib2
import json

filePath = "D:/projects/VoiceManager/com/work/voiceManager/output.flac"
GOOGLE_SPEECH_URL_V2 = "https://www.google.com/speech-api/v2/recognize?output=json&lang=ru-RU&key=AIzaSyCCBnLCZAtUcVHi94fRklcc3VOMeYzgFDs";
hrs = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7",
 'Content-type': 'audio/x-flac; rate=16000'} 
f = open(filePath, 'rb')
flac_cont = f.read()
f.close()
req = urllib2.Request(GOOGLE_SPEECH_URL_V2, data=flac_cont, headers=hrs)
print "Sending request to Google TTS"
p = urllib2.urlopen(req)
response = p.read()
response = response.split('\n', 1)[1]
print response
# Try to get something out of the complicated json response:
#res = json.loads(response)['result'][0]['alternative'][0]['transcript']
 

 
