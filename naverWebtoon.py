from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text,"html.parser")

#pprint(soup)

data1=soup.find('div',{'class':'col_selected'})
# pprint(data1)


data2=data1.findAll('a',{'class':'title'})
# pprint(data2)

titleList =[]
for i in data2 :
    titleList.append(i.text)
    pprint(" Hello Github")

pprint(titleList)
