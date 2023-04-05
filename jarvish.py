import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
import wikipedia
import pywhatkit
import os
import sys
import keyboard
import playsound
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)

def speak(audio):
    print(' ')
    Assistant.say(audio)
    print(f":{audio}")
    print(' ')
    Assistant.runAndWait()
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()


    def takecommand(self):
        command=sr.Recognizer()
        with sr.Microphone() as source:

            print("Listening..............")
            command.pause_threshold-1
            audio=command.listen(source)

        try:
            print("Recognizing..........")
            self.query=command.recognize_google(audio,language='en-in')
            print(f'You said:{self.query}')

        except Exception as Error:
            return "none"
        return self.query.lower()
        #return self.query

    def TaskExecution(self):

        while True:
            self.query=self.takecommand()
            if "hello" in self.query:
                speak("Hello Sir, I Am jarvish")
                speak("Your Personal Ai Assistant !")
                speak("How may i help you? ")

            elif "how are you" in self.query:
                speak("i am fine sir !")
                speak("what's About you?")

            elif "you need a break" in self.query:
                speak("ok sir, you can Call me Anytime ! ")
                break

            elif "bye" in self.query:
                speak("ok sir,Bye")
                break
    #taskExe()
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=  Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie =QtGui.QMovie("../../../../Downloads/Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie =QtGui.QMovie("../../../../Downloads/Code_Template.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie =QtGui.QMovie("../../../../Downloads/jarvish gui/initial.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start()
        
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
app =QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

