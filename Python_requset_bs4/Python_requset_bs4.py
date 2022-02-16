'''
抓出yahoo奇摩新聞首頁標題
'''

from bs4 import BeautifulSoup
import requests

r = requests.get('https://tw.yahoo.com/')
if r.status_code == requests.codes.ok:
    
    #用BeautifulSoup解析HTML程式碼
    soup = BeautifulSoup(r.text , 'html.parser')
    
    #以CSS的class抓出各類頭條新聞
    stories = soup.find_all('li' , class_="List(n) Mb(12px) Mah(42px)" , limit=10)
    
    for i in range(5,10):
        #新聞標題
        print("標題: " + stories[i].text)