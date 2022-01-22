import requests
from bs4 import BeautifulSoup

url = 'http://section.cgv.co.kr/theater/timetable/Default.aspx?code=0013'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

s = soup.select('table > tbody > tr > td > a > span ')
c = soup.select('table > tbody > tr ')

#for i, item in enumerate(s):
    #print(item.attrs['title'])


imax = 0

for t in c:
    for i, item in enumerate(t):
        #print(i, item)
        imax = 0
        if i == 1: # title
            tmp = item.select('a > span')
            for p in tmp:
                print(p.attrs['title'], end = "")
            #print(tmp.attrs['title'])
        if i == 3: # n관
            if item.select('img') != None:
                img = item.select('img')
                for m in img:
                    #print(m['src'])
                    if m['src'] == "http://img.cgv.co.kr/theater_img/theater_icon_07.gif":
                        imax = 1
                        print("IMAX")
                if imax != 1:
                    print(item.text)
    print("======================================")
