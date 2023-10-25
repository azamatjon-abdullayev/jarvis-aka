import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {
    "alias":("jarvis", 'salom','jarvis', 'jar', 'jorvis', 'jarviz', 'jorviz'),
    "tbr":('aytginchi', "ko'rsatchi", 'korsat', 'aytchi'),
    "cmds": {
        "ctime": ('xozirgi vaqt', 'soat nechi', 'xozir vaqt'),
        "radio": ("muzika qo'y", 'radioni yoq'),
        "stupid1": ('latifa aytib ber', 'meni kuldir', 'yoshim nechida')
}
}

def speak(what):
    print(what)
    speek_engine.say(what)
    speek_engine.runAndWait()
    speek_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="uz-UZ").lower()
        print("[log] atildi: " + voice)

        if voice.startswith(opts["alias"]):
            cmd = voice

            for x in opts["alias"]:
                cmd = cmd.replace(x, "").strip()
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            cmd = recognizer_cmd(cmd)
            execute_cmd(["cmd"])
    except sr.UnknownValueError:
        print("[log] Tushunarsiz gap")

    except sr.RequestError as e:
        print("[log] Tushunarsiz gap, Internetni tekshiring")



def recognizer_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
            return RC
def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak(" hozirgi vaqt " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':

        os.system("D:\\Тохир Содиков - Ajoyib kun.mp3")


r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as sourse:
    r.adjust_for_ambient_noise(sourse)
speek_engine = pyttsx3.init()

voices = speek_engine.getProperty("voices")
speek_engine.setProperty('voice', voices[0].id)


speak('salom dastur')

stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)