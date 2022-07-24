import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import os.path
import smtplib
import cv2
import random
from requests import get
import pywhatkit as kit
import sys
import time
import urllib.request
import pyjokes
import pyautogui
import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import requests
import instaloader
import instadownloader
import operator
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Minor import Ui_Minor


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voice', voices[2].id)

def speak(talk):
    engine.say(talk)
    engine.runAndWait()

    # This function tells the news but has little bug in it.

# def news():
    # main_url = 'http://newsapi.org/v2/top-headlines?source=techcrunch&apiKey=0d6d9f88492245e7b6c0016d796a3b82'

    # main_page = requests.get(main_url).json()

    # acticles = main_page("articles")

    # head=[]

    # day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    # for ar in articles:
    #     head.append(ar["title"])

    # for i in range (len(day)):
    #     speak(f"today's {day[i]} news is: {head[i]}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >=0 and hour<12:
        speak(f"Good Morning Ritik Sir!, its {tt}")
    elif hour>=12 and hour<16:
        speak(f"Good Afternoon Ritik Sir! , its {tt}")
    else:
        speak(f"Good Evening Ritik Sir! , its {tt}")


    speak("How can i help you sir?")

#THIS FUNCTION IS USED TO SEND EMAIL.

# def sendEmail(to, content):
    # server = smtplib.SMTP('smpt.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login(YOUR EMAIL, PASSWORD OF EMAIL)
    # server.sendmail(FRIEND'S EMAIL ADD., to, content)
    # server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()  


    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0)
            print("Listening...")
            #r.pause_threshold = 1
            r.energy_threshold = 250
            audio = r.listen(source,timeout=5,phrase_time_limit=8)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            speak("say that again please ...")
            return "none"
        return query

    def TaskExecution(self):
        wishMe()
        while True:

            self.query = self.takeCommand().lower()

            if 'tell me about' in self.query:
                speak('searching wikipedia...')
                #query = query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=5)
                print(resutl)
                speak("According to wikipedia")
                speak(result)
            elif 'in wikipedia' in self.query or 'search wikipedia' in self.query or 'search about' in self.query:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=5)
                print(result)
                speak("According to wikipedia")
                speak(result)
            elif 'who are you' in self.query:
                print('I am your AI Voice assistant. I have been created by Ritik sir and his team for their personal use so i am customized according to that. If you want you can customize me according to your needs.')
                speak('I am your AI Voice assistant. I have been created by Ritik sir and his team for their personal use so i am customized according to that. If you want you can customize me according to your needs.')
            elif 'can you do' in self.query:
                print('i can search wikipedia for you, i can play songs on youtube, i can open youtube,notepad,command prompt, camera, google, geeks for geeks, stack overflow, hackerrank, hackerearth, linkedin, pycharm, i can tell you ip address of this machine, i can send whatsapp message for you, i can search anything for you on internet, i can tell you a joke, i can shut down and restart the system and i can switch between different windows, i can even tell you your location along with longitude and latitude , can take screenshot and i can even look up for any instagram profile you want, even download their profile picture.')
                speak('i can search wikipedia for you, i can play songs on youtube, i can open youtube,notepad,command prompt, camera, google, geeks for geeks, stack overflow, hackerrank, hackerearth, linkedin, pycharm, i can tell you ip address of this machine, i can send whatsapp message for you, i can search anything for you on internet, i can tell you a joke, i can shut down and restart the system and i can switch between different windows, i can even tell you your location along with longitude and latitude , can take screenshot and i can even look up for any instagram profile you want, even download their profile picture.')
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
            elif 'open notepad' in self.query:
                nppath = "C:\\Windows\\notepad.exe"
                os.startfile(nppath)
            elif 'close notepad' in self.query:
                os.system("taskkill /f /im notepad.exe")
            elif 'open command prompt' in self.query:
                os.system("start cmd")
            elif 'close command prompt' in self.query:
                os.system("taskkill /f /im cmd.exe")
            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif 'my ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")
            elif 'open google' in self.query:
                speak("what should i search on google")
                comm = self.takeCommand().lower()
                webbrowser.open(f"{comm}")
            elif 'send whatsapp message' in self.query:
                speak("please tell me the contact number sir!")
                cnum = self.takeCommand().lower()
                speak("what message would you like me to send")
                smsg = self.takeCommand().lower()
                kit.sendwhatmsg(f"+91{cnum}", f"{smsg}",22,30)
            elif 'open geeksforgeeks' in self.query or 'open geeks for geeks' in self.query:
                webbrowser.open("geeksforgeeks.org")
            elif 'open stack overflow' in self.query or 'open stackoveflow' in self.query:
                webbrowser.open("stackoverflow.com")
            elif 'open hackerrank' in self.query or 'open hacker rank' in self.query:
                webbrowser.open("hackerrank.com")
            # elif 'send email to yash' in self.query:
            #     try:
            #         speak("What should i say?")
            #         content = self.takeCommand().lower()
            #         to = EMAIL ADD OF RECIPIENT
            #         sendEmail(to, content)
            #         speak("Email has been sent! sir")
            #     except Exception as e:
            #         print(e)
            #         speak("sorry i am unable to send the email right now")
            # elif 'send email' in self.query:
            #     speak("sir what should i say")
            #     query = self.takeCommand().lower()

            #     if "send a file" in self.query:
            #         email = YOUR EMAIL
            #         password = PASSWORD
            #         send_to_email = RECIPIENT EMAIL
            #         speak("okay sir!, what is the subject for this email")
            #         query = self.takeCommand().lower()
            #         subject = query
            #         speak("and sir, what is the message for this email")
            #         query2 = self.takeCommand().lower()
            #         message = query2
            #         speak("sir  please enter the correct part of the file into the shell")
            #         file_location = input("please enter the path here")

            #         speak("please wait, i am sending the email now")

            #         msg = MIMEMultipart()
            #         msg['From'] = email
            #         msg['To'] = send_to_email
            #         msg['Subject'] = subject

            #         msg.attach(MIMEText(message, 'plain'))

            #         filename = os.path.basename(file_location)
            #         attachment = open(file_location, "rb")
            #         part = MIMEBase('application', 'octet-stream')
            #         part.set_payload(attachment.read())
            #         encoders.encode_base64(part)
            #         part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            #         msg.attach(part)

            #         server = smtplib.SMTP('smtp.gmail.com', 587)
            #         server.starttls()
            #         server.login(email, password)
            #         text = msg.as_string()
            #         server.sendmail(email,send_to_email, text)
            #         server.quit()
            #         speak("email has been sent sir")
            #     else:
            #         email = YOUR EMAIL
            #         password = PASSWORD
            #         send_to_email = RECIPIENT EMAIL
            #         message = query
            #         server = smtplib.SMTP('smtp.gmail.com', 587)
            #         server.starttls()
            #         server.login(email, password)
            #         text = msg.as_string()
            #         server.sendmail(email,send_to_email, text)
            #         server.quit()
            #         speak("email has been sent sir")


            
            elif 'open hackerearth' in self.query or 'open hacker earth' in self.query:
                webbrowser.open("hackerearth.com")
            elif 'open linkedin' in self.query or 'open linked in' in self.query:
                webbrowser.open("in.linkedin.com")
            elif 'play music' in self.query:
                music_dir = ''
                songs = os.listdir(music_dir)
                print(songs)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'what is the time' in self.query or 'tell me the time' in self.query or 'show me the time' in self.query or 'what is time' in self.query or 'tell me time' in self.query or 'show me time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            elif 'play video on youtube' in self.query:
                speak("please tell me the name of that video")
                vname = self.takeCommand().lower()
                kit.playonyt(f"{vname}")
        
            elif 'open pycharm' in self.query:
                pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
                os.startfile(pycharmPath)
        
            
            elif 'ok quit' in self.query or 'ok sleep' in self.query or 'ok stop' in self.query or 'stop' in self.query or 'quit' in self.query:
                speak("Thank you sir")
                sys.exit()
            elif 'tell me a joke' in self.query or 'tell me the joke' in self.query or 'tell me joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif 'shut down the system' in self.query or 'shut down system' in self.query or 'shut down' in self.query:
                os.system("shutdown /s /t S")
            elif 'restart the system' in self.query or 'restart system' in self.query:
                os.system("shutdown /r /t S")
            elif 'switch the window' in self.query or 'switch window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            # elif 'read news' in self.query:
            #     speak("please wait sir, fetching the latest news")
            #     news()
            elif 'make system sleep' in self.query or 'sleep' in self.query or 'sleep system' in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'where am i' in self.query or 'where are we' in self.query or 'where i am' in self.query or 'tell me my location' in self.query or 'what is my location' in self.query or 'my location' in self.query:
                speak("Let me check sir")
                try:
                    ipAddress = requests.get('https://api.ipify.org').text
                    print(ipAddress)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAddress + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    state = geo_data['region']
                    country = geo_data['country']
                    latitude = geo_data['latitude']
                    longitude = geo_data['longitude']
                    speak(f"sir we are in {city} city of state {state}, country {country} and our latitude is {latitude} and longitude is {longitude}")
                except Exception as e:
                    speak("Sorry sir, due to network issue i am unable to find our location")
                    pass

            elif 'instagram profile' in self.query or 'profile on instagram' in self.query or 'profile in instagram' in self.query:
                speak("sir please enter the account's user name")
                name  = input("Enter username here :")
                webbrowser.open(f"www.instagram.com/{name}")
                speak("sir here is the profile you are looking for")
                time.sleep(3)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak(" Profile picture is saved in our main folder sir")
                else:
                    pass

            
            elif 'take screenshot' in self.query or 'take a screenshot' in self.query or 'click a screenshot' in self.query or 'click screenshot' in self.query or 'click the screenshot' in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name  = self.takeCommand().lower()
                speak("please wait i am taking the screenshot")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in the main folder")
            else:
                print('Here is what i found on the internet..')
                speak('Here is what i found on the internet..')
                #search = 'https://www.google.com/search?q=',self.query
                webbrowser.open('http://www.google.com/search?btnG=1&q=%s' % self.query)

            speak("I am done sir!, anything else sir!")
  

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Minor()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.startTask)
        self.ui.Start_2.clicked.connect(self.close)
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("bk.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("initiate system.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time =current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
voiceAssist = Main()
voiceAssist.show()
exit(app.exec_())