from gtts import gTTS
import os
from playsound import playsound
# Python3 code to convert a tuple
# into a string using str.join() method
def convertTuple(appusername):
	str = ''.join(appusername)
	return str
	tuplea = appusername
	str = convertTuple(tuplea)
	print(str)

def welcome (appusername):
	welcomemsg="Hello"+appusername+".welcome to ARASAN AI"
	language="hi"
	myobj = gTTS(text=welcomemsg, lang=language, slow=False)
	myobj.save("sayloaded.mp3")
	playsound('sayloaded.mp3')
def opening (app_name):
	opening="Opening"+app_name
	language="hi"
	myobj = gTTS(text=opening, lang=language, slow=False)
	myobj.save("opening.mp3")
	playsound("opening.mp3")