# import pyttsx3 #pip install SpeechRecognition
# gap = pyttsx3.init() #pip install pyttsx3
# gap.say('azamatjon dasturchi') #pip install pywin32
# gap.runAndWait()
#/////////////////////////////////

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for ".format(index, name))

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as sourse:
    print('Nimadir ayting')
    audio = r.listen(sourse)

query = r.recognize_google(audio, language="uz-UZ")
print(f"siz {query.lower()} dedingiz")