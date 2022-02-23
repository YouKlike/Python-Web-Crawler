from bs4 import BeautifulSoup

#requsets模組是用來處理HTTP請求
import requests

#收集中獎樂透的編號
winning_Numbers_Sort_lotto = ['Lotto649Control_history_dlQuery_SNo1_0']


def search_winning_numbers(css_class):
    #宣告一個全域變數
    global winning_Numbers_Sort_lotto
    
    #透過CSS搜尋詢者指定CSS類名的tag
    if (css_class != None):
        for i in range(len(winning_Numbers_Sort_lotto)):
            if winning_Numbers_Sort_lotto [i] in css_class:
                return css_class
    
head_Html_lotto = 'http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'

#使用GET方式下載普通網頁,如果等待超過30秒則取消
res = requests.get(head_Html_lotto , timeout=30)

#lxml是用來解析requests取得的數據
soup = BeautifulSoup(res.text, 'lxml')

#搜尋所有為 search_winning_numbers 的字串並存入到 header_Info
header_Info = soup.find_all(id=search_winning_numbers)

#列印所有字串
for i in header_Info:
    print(i)