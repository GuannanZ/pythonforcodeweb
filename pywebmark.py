import requests
import csv
from bs4 import BeautifulSoup

def connect(DATA,HEADERS):
    S = requests.Session()
    S.post('http://smoj.nhedu.net/login',data=DATA,headers=HEADERS)
    r = S.get("http://smoj.nhedu.net/ShowAllSubmits")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(ilt,html):
    try:
        soup = BeautifulSoup(html,'lxml')
        trs =soup.find_all('tr',class_='active')
        length = len(trs)
        for i in range(length):
            usename = trs[i].contents[1].a.text
            problemid = trs[i].contents[3].a.text
            status = trs[i].contents[5].text
            language = trs[i].contents[7].string.replace(' ','').replace('\n','')
            time = trs[i].contents[9].string
            result = trs[i].contents[11].a.text
            ilt.append([ usename ,problemid,status, language, time, result])
    except:
        return ''

def save_contents(urlist):
    with open("D:/成绩.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(['成绩'])
        for i in range(len(urlist)):
            writer.writerow([urlist[i][0],urlist[i][1],urlist[i][2],urlist[i][3],urlist[i][4]])
def main():
    infolist = []
    DATA = {"username": 'username', "password": 'password'}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    html = connect(DATA, HEADERS)
    infolist.append(['用户名', '题目ID', '测评状态', '使用语言', '提交时间', '得分/总分', ])
    parsePage(infolist, html)
    save_contents(infolist)
main()


