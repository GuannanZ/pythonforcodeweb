import requests
import re
import pandas as pd

def connect(DATA,HEADERS):
    S = requests.Session()
    S.post('http://smoj.nhedu.net/login',data=DATA,headers=HEADERS)
    r = S.get("http://smoj.nhedu.net/ShowAllSubmits")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(ilt, html):
    try:
        plt = re.findall('<tr class="active">.*?</tr>', html)
        l = len(plt)
        l = l // 6
        for i in range(l):
            j = i * 6
            name = plt[j + 1].split('">')[1].split('<')[0]
            questionnum = plt[j + 2].split('&nbsp;')[1].split('<')[0]
            doneornot = plt[j + 3].split('">')[1].split('<')[0]
            language = plt[j + 4].split('">')[1].split('<')[0]
            time = plt[j + 5].split('">')[1].split('<')[0].replace('&nbsp;', '')
            mark = plt[j + 6].split('">')[1].split('<')[0]
            ilt.append([name, questionnum, doneornot, language, time, mark])
    except:
        return ''

def saveGoodslist(ilt):
    pd.DataFrame(ilt).to_csv('成绩.csv', index=False, header=False)

def main():
    infolist = []
    DATA = {"username": 'username', "password": 'password'}
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    html = connect(DATA, HEADERS)
    infolist.append(['用户名', '题目ID', '测评状态', '使用语言', '提交时间', '得分/总分'])
    parsePage(infolist, html)
    saveGoodslist(infolist)
main()


