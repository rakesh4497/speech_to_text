from cgi import test
import speech_recognition as sr
import json 
from datetime import datetime

r = sr.Recognizer()
run = True
mic = sr.Microphone()
data = {}
# timestamp = str(datetime.now())


with open("notepad.json","r") as f:
    data = json.load(f)

while run:    
    print('start speaking')
    with mic as source:
        audio_text = r.listen(source)
        #text=r.recognize_google(audio_text)
        #print(text)
        try:
            text=r.recognize_google(audio_text)
            print(json.dumps(data,indent=4))
            timestamp = datetime.now()
            data["notes"].append({str(timestamp):text})
            with open("notepad.json","w") as outfile:
                outfile.write(json.dumps(data, indent=4))
        except KeyboardInterrupt:
            print("stopping")         
        except:
            print("error")
            run=False
