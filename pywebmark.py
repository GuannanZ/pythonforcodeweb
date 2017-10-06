import pandas as pd
import requests
LOGIN_URL = 'http://smoj.nhedu.net/login'
DATA = {"username":'username',"password":'password'}# username填用户名，password填密码
HEADERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
           }
def Get_Session(URL,DATA,HEADERS):
    ROOM_SESSION  = requests.Session()
    ROOM_SESSION.post(URL,data=DATA,headers=HEADERS)
    return ROOM_SESSION
SESSION =Get_Session(LOGIN_URL,DATA,HEADERS)
RES = SESSION.get("http://smoj.nhedu.net/ShowAllSubmits")
data =pd.read_html(RES)[0]
def saveGoodslist(ilt):
    pd.DataFrame(ilt).to_csv('TEST1.csv',index=False,header=False)
print(RES.text)