import os
import eel
eel.init('frontend') # Point to your folder name
eel.start('index.html')
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *

def start():

    eel.init("frontend")

    play_assistant_sound()
    @eel.expose
    def init():
        eel.hideLoader()
        speak("Welcome to Jarvis")
        speak("Ready for face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag ==1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak("Welcome to your Assistant")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")

    os.system('start mschrome.exe --app = "http://127.0.0.1:5500/frontend/index.html" ')

   

    eel.start("index.html",mode=None, host="localhost",block=True)
