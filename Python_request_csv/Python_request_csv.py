import urllib.request,csv
url ='https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'
webpage = urllib.request.urlopen(url) #開啟網頁
#讀取資料到data陣列中,請留意csv檔案的編碼方式
data = csv.reader(webpage.read().decode('big5').splitlines())
 
for i in data:
    if i[4] in '金門縣':
        print('年分->',i[0],'名稱->',i[2],'景點=',i[3], '總計人數=',i[17])