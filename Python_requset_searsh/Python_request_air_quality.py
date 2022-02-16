import urllib.request as req
import json

src = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

with req.urlopen(src) as rsp:
    data = json.load(rsp)

search = input("請輸入要查詢的站名: ")
mylist = data['records']
for exh in mylist:
    if (exh["SiteName"].find(search)) >= 0:
        print("縣市: " , exh['County'] , "\t空氣品質指標AQI: " , exh['AQI'] , "\n狀態: " , exh['Status'] , "\t時間: " , exh['PublishTime'] )