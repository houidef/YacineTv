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


data = getURL("http://yacinelive.com/api/categories")
#print(convert(ndata))
#file.write(data)
s = convert(data)
js = json.JSONDecoder().decode(s)
js = js['data']
for ch in js:
	print(ch['id'],ch['name'])

x = input()
data = getURL("http://yacinelive.com/api/getChannelsByCategory/"+x)
s = convert(data)
js = json.JSONDecoder().decode(s)
js = js['data']
#print(js)
for ch in js:
	print(ch['id'],ch['name'])
x = input()
data = getURL("http://yacinelive.com/api/channel/"+x)
s = convert(data)
js = json.JSONDecoder().decode(s)
js = js['data']
playlists = set(['m3u8'])

Instance = vlc.Instance()
for ch in js:
    print(ch['name'],ch['url'])
    media = vlc.MediaPlayer(ch['url'])
    media.play()
    sleep(15000)

	

#if x == '1' :
#	print("XXXXXXX")
#file.write(s.encode('utf8'))
#file.close()