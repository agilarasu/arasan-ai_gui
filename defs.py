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
	myobj.save("welcome.mp3")
	playsound('welcome.mp3')
