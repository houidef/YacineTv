###### The code will be published soon
###### Greetings from Houidef Abdelkader
###### We regret not publishing the source code because that would quickly change the current version of the application.
import urllib.request
import base64
import numpy as np
import json
import vlc
from time import sleep,ctime,time
from datetime import datetime
url = "a500.variety-buy.store"
def convert(s):
    new = ""
    for x in s:
        new += x 
    return new
ef crpt(data,r):
    i = 0
    ndata = []
    pswrd = ############### The code will be published soon
    '''
    The code will be published soon
    '''
    return convert(ndata)

def getURL(url,r0):
    print(url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'okhttp/3.12.8')
    response = urllib.request.urlopen(req)
    r = ########The code will be published soon
    data = response.read()
    data = base64.b64decode(data)
    text = data.decode("utf-8")
    return crpt(text,r)
    
#testing:
print('config:----------------------------------------------------------')
data = getURL("https://a500.variety-buy.store/api/config?code=","")
print(data)
exit()
print('categories:----------------------------------------------------------')
data = getURL("https://a500.variety-buy.store/api/categories","")
print(data)

print('categories NB:----------------------------------------------------------')
key=str(int(time()))+'d'
data = getURL("https://a500.variety-buy.store/api/categories/9","")
print(data)
print('categories NB:----------------------------------------------------------')
key=str(int(time()))+'d'
data = getURL("https://a500.variety-buy.store/api/categories/14/channels","")
print(data)

print('player:----------------------------------------------------------')
data = getURL("https://a500.variety-buy.store/api/config/player","")
print(data)

print('channel:----------------------------------------------------------')
data = getURL("https://a500.variety-buy.store/api/channel/505","m")
print(data)

print('channel:----------------------------------------------------------')
data = getURL("http://a500.variety-buy.store/api/channel/1422","")
print(data)

print('search:----------------------------------------------------------')
data = getURL("http://a500.variety-buy.store/api/search","")
print(data)

print('events:----------------------------------------------------------')
data = getURL("http://a500.variety-buy.store/api/events","")
print(data)
