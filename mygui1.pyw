import PySimpleGUI as sg
sg.theme('dark grey 9')
import urllib.request
import base64
import numpy as np
import json
import vlc
from time import sleep
url = "http://yacinelive.com/api/events"
url = "http://yacinelive.com/api/categories"
#url = "http://yacinelive.com/api/search"
#url = "http://yacinelive.com/api/config"
#url = "http://yacinelive.com/api/getChannelsByCategory/1"
#url = "http://yacinelive.com/api/channel/6"
l = []
mych = []
mySer = []
NumCat = []
Num2 = []
Num3 = []
def convert(s):
    new = ""
    for x in s:
        new += x 
    return new
	
def crpt(data):
	i = 0
	ndata = []
	pswrd = "c!xZj+N9&G@Ev@vw"
	while (i<len(data)):
		k = chr(ord(data[i])^ord(pswrd[i%16])) 
		ndata.append(k)
		i = i+1
	return convert(ndata)
def getURL(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0')
	response = urllib.request.urlopen(req)
	data = response.read()
	data = base64.b64decode(data)
	text = data.decode("utf-8")
	return crpt(text)
	#file = open(r"MyFile.txt","wb")
#np.chararray(len(data))
def ListCategories():
    l.clear()
    mych.clear()
    mySer.clear()
    NumCat.clear()
    Num2.clear()
    Num3.clear()
    data = getURL("http://yacinelive.com/api/categories")
    #file.write(data)
    s = convert(data)
    js = json.JSONDecoder().decode(s)
    js = js['data']
    for ch in js:
       l.append(str(ch['id'])+'   :'+str(ch['name']))
       NumCat.append(ch["id"])
    #print(NumCat)

def GetChannelsByCategory(x):
   mych.clear()
   Num2.clear()
   mySer.clear()
   Num3.clear()
   data = getURL("http://yacinelive.com/api/getChannelsByCategory/"+x)
   s = convert(data)
   js = json.JSONDecoder().decode(s)
   js = js['data']
   for ch in js:
       mych.append(str(ch['id'])+'   :'+str(ch['name']))
       Num2.append(ch["id"])
   window['combo2'].update(value='', values=mych)

def getchannel(x):
   Num3.clear()
   mySer.clear()
   data = getURL("http://yacinelive.com/api/channel/"+x)
   s = convert(data)
   js = json.JSONDecoder().decode(s)
   js = js['data']
   playlists = set(['m3u8'])
   Instance = vlc.Instance()
   k=1
   for ch in js:
      mySer.append('Server Number '+str(k)+'   :'+str(ch['url']))
      Num3.append(ch["url"])
      k = k+1
   window['combo3'].update(value='', values=mySer)

ListCategories()
# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("Channel Categorie:")],
		  [sg.Combo(l, size=(70, 10), enable_events=True, key='combo')],
          [sg.Text("Channel:")],
          [sg.Combo(mych, size=(70, 10), enable_events=True, key='combo2')],
          [sg.Text("Server Name")],
          [sg.Combo(mySer, size=(70, 10), enable_events=True, key='combo3')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Stop'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Yacine Tv', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == 'combo' :
       GetChannelsByCategory(str(NumCat[l.index(values['combo'])]))
       #print(NumCat)
       window['-OUTPUT-'].update('categories : ' + values['combo'])
    if event == 'combo2' :
       getchannel(str(Num2[mych.index(values['combo2'])]))
    if event == 'combo3' :
       if 'media' in locals(): media.stop()
       media = vlc.MediaPlayer(Num3[mySer.index(values['combo3'])])
       media.play()
       #print('channel is play')
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Stop':
         #print('stop')
         if 'media' in locals(): media.stop()
    # Output a message to the window
    #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()