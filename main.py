import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from defs import *
from subprocess import call
def clear():
	_ = call('clear')
   
class Ui_ARASAN(object):
    def startai(self):
        start_assistant()
    def stopai(self):
        print("stop")
    def contactus(self):
        print("contact")
    def exitai(self):
        sys.exit()
    def setupUi(self, ARASAN):
        ARASAN.setObjectName("ARASAN")
        ARASAN.resize(1169, 512)
        ARASAN.setAutoFillBackground(False)
        ARASAN.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        ARASAN.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(ARASAN)
        self.centralwidget.setObjectName("centralwidget")
        #start btn
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(880, 130, 121, 51))
        self.START.setStyleSheet("background-color: rgb(255,255,255)")
        self.START.setObjectName("START")
        self.START.clicked.connect(self.startai)
        #stopbtn
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 200, 121, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255,255,255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.stopai)
        #contact btn
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 270, 121, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255,255,255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.contactus)
        #exit btn
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 340, 121, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(255,255,255)\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.exitai)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -40, 1431, 671))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Arasan.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.raise_()
        self.START.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        ARASAN.setCentralWidget(self.centralwidget)

        self.retranslateUi(ARASAN)
        QtCore.QMetaObject.connectSlotsByName(ARASAN)

    def retranslateUi(self, ARASAN):
        _translate = QtCore.QCoreApplication.translate
        ARASAN.setWindowTitle(_translate("ARASAN", "Arasan AI"))
        self.START.setText(_translate("ARASAN", "Start"))
        self.pushButton.setText(_translate("ARASAN", "Stop"))
        self.pushButton_2.setText(_translate("ARASAN", "Contact Us"))
        self.pushButton_3.setText(_translate("ARASAN", "Exit"))


#assistant
def start_assistant():
    import speech_recognition as sr
    from lxml import html
    import requests
    import webbrowser
    import os
    from pynput.keyboard import Key, Controller
    import mouse
    from gtts import gTTS
    from playsound import playsound
    from subprocess import call
    from time import sleep
    import csv
    mlist = []
    loopme = 1
    r = sr.Recognizer()
    keyboard = Controller()
    settings_line = 1
    with open('csv/userdetails.csv', 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        name_userdetials = mycsv[settings_line][0]
        print(name_userdetials)
        appusername=name_userdetials
        welcome(appusername)
        print("Hello ",appusername,"! \nWelcome To ARASAN AI")
        loopme=1
        while(loopme == 1):
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                clear()
                print("Say Something....")
                print("Try: Open (youtube/twitter/insta) \nTry: exit assistant #to close assistant")
                audio = r.listen(source)
                print("Trying to recognize Your Voice...")
                t = r.recognize_google(audio).lower()
                print("You just said "+t)

            try:
                if(t.find("open") != -1):
                    le = t.find("open")+len("open")+1
                    t = t[le:]
                    if (t=="youtube" or t=="Youtube"):
                        nrow=1
                    elif (t=="twitter" or t=="Twitter"):
                        nrow=2
                    elif (t=="instagram" or t=="insta"):
                        nrow=3
                    try:
                        with open('csv/webapps.csv', 'r') as f:
                            mycsv = csv.reader(f)
                            mycsv = list(mycsv)
                            text = mycsv[nrow][1]
                            print(text)
                            app_name=mycsv[nrow][0]
                            print("Opening ",text)
                            exec(open(text).read())
                    except:
                        print("Cannot open \n"+t+"Check if it is installed")
                if(t.find("exit") != -1):
                    le = t.find("exit")+len("exit")+1
                    t = t[le:]
                    if (t=="A I" or t=="assistant"):
                        loopme=0
                        
            
            except:
                print("Cannot Open")
        if loopme==0:
            sys.exit()
#end assistant



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ARASAN = QtWidgets.QMainWindow()
    ui = Ui_ARASAN()
    ui.setupUi(ARASAN)
    ARASAN.show()
    sys.exit(app.exec_())
            