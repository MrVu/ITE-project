import requests, os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from uuid import getnode as get_mac
from gtts import gTTS
from gpiozero import Button
from signal import pause

tmpNum = ''

button1 = Button(23)
button2 = Button(18)

def userChoice():
    global tmpNum
    mac_address = get_mac()
    while 1:
        if(button1.when_pressed == True):
            b1Pressed(mac_address)
        elif(button2.when_pressed == True):
            b2Pressed()

def playViLanguage(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("tmp.mp3")
    os.system("mpg321 tmp.mp3")


def b1Pressed(mac_address):
    postRequest = requests.post('http://45.117.169.186:8000/api_1_0/first_data', data = {'mac_address':mac_address})
    return_data = postRequest.json().get('return_data')
    num = return_data.get('num')
    if num == 0:
        playResult('No answer yet')
    else:
        result = return_data.get('result')
        text = 'Câu ' + str(num) + ': ' + result
        playViLanguage(text)
        tmpNum = text


def b2Pressed():
    if tmpNum == '':
        playViLanguage('Chưa có câu trả lời mới')
    else:
        os.system("mpg321 tmp.mp3")

if __name__ == '__main__':
    userChoice()
