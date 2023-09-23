from NIX import NIXAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import pyjokes
import time
import pyautogui
import pywhatkit
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from NIX.features.gui import Ui_MainWindow
from NIX.config import config

obj = NIXAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hey buddy", "hey", "wake up buddy",
             "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]
# =======================================================================================================================================================


def speak(text):
    obj.tts(text)

def startup():
    speak("Initializing NIX")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am NIX. Online and ready sir. Please tell me how may I help you")
    speak("Sir i want to tell you that i am in a building stage so i have some bugs if you face any please forgive me")
    speak("So sir if you want to know what are my features then please check the text file i have opened")




# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")



            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)


            elif re.search('about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try something else")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: BBC NEWS')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif 'search google for' in command:
                obj.search_anything_google(command)
            


            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            
            elif "what is" in command or "who is" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)

            

            if "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that")

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad++.exe")

            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system information" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "shutdown the computer" in command or "shutdown" in command:
                speak("Okay sir, Going to shutdown the window")
                pyautogui.hotkey('alt','f4')
                pyautogui.press('enter')
                pyautogui.hotkey('alt','f4')
                pyautogui.press('enter')
                pyautogui.hotkey('alt','f4')
                pyautogui.press('enter')

            elif "Restart" in command:
                speak("Okay sir ,Going to restart the window")
                pyautogui.hotkey('win' 'r')
                pyautogui.typewrite('powershell')
                pyautogui.hotkey('enter')
                pyautogui.typewrite('Restart-Computer -Force')
                pyautogui.hotkey('enter')

            elif "cam" in command or "camera" in command or "live" in command or "view" in command or "lens" in command:
                speak("Okay sir opening the live camera access , for example russia")
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('chrome http://www.insecam.org/en/view/508606/')
                pyautogui.hotkey('enter')

            elif "radio" in command:
                speak("Okay sir i am giving you access to the radios of all over the world")
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('chrome http://radio.garden/visit/silchar/vw4-uvxr')
                pyautogui.hotkey('enter')
                time.sleep(10)
                pyautogui.hotkey('win' 'r')
                pyautogui.typewrite('cmd')
                pyautogui.hotkey('enter')
                pyautogui.typewrite('cd Desktop/NIX/NIX/NIX/Features ; python click_mouse.py 100 1000')
                pyautogui.typewrite('enter')

            elif "virus" in command:
                speak("Okay sir opening the site to check whether your files have trojans or not and i am using some of your files as an example.")    
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('powershell')
                pyautogui.hotkey('enter')
                time.sleep(5)
                pyautogui.typewrite('cd Desktop')
                pyautogui.hotkey('enter')
                pyautogui.typewrite('Start-Process PRIYANSU.lnk ; python click_mouse.py 500 50')
                pyautogui.hotkey('enter')
                time.sleep(5)
                pyautogui.typewrite('https://www.virustotal.com/gui/home/upload')
                pyautogui.hotkey('enter')
                time.sleep(4)
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('powershell')
                pyautogui.hotkey('enter')
                time.sleep(3)
                pyautogui.typewrite('cd Desktop/NIX/NIX/NIX/Features ; python click_mouse.py 1370 80 ; python click_mouse.py 900 765')
                pyautogui.hotkey('enter')
                time.sleep(3)
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('powershell')
                pyautogui.hotkey('enter')
                time.sleep(3)
                pyautogui.typewrite('cd Desktop/NIX/NIX/NIX/Features ; python click_mouse.py 1370 80 ; python click_mouse.py 400 310')
                pyautogui.hotkey('enter')
                time.sleep(3)
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('powershell')
                pyautogui.hotkey('enter')
                time.sleep(3)
                pyautogui.typewrite('cd Desktop/NIX/NIX/NIX/Features ; python click_mouse.py 1370 80 ; python click_mouse.py 780 570')
                pyautogui.hotkey('enter')

            elif "cyber attacks" in command:
                speak("Okay sir opening the live site to check the purpose of cyberattacks")    
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('chrome https://www.fireeye.com/cyber-map/threat-map.html')
                pyautogui.hotkey('enter')
                

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command or "show" in command:
                try:
                    img = Image.open('C:/Users/PRIYANSU/Desktop/NIX/NIX/' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")


            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you PRIYANSU sir")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("NIX/utils/images/miguel.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("NIX/utils/images/INT.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
nix = Main()
nix.show()
exit(app.exec_())
