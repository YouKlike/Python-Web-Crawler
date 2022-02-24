import urllib.request as req
import json

src = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

with req.urlopen(src) as rsp:
    data = json.load(rsp)

search = input("請輸入查詢站名:")
for s in data:
    if (s["sna"].find(search)) >= 0:
        print(s["sarea"]
              +" 站名: "+s["sna"]+"\t目前數量: "
              ,s["sbi"],"\n空位數量: ",s["bemp"]
              ,"\t時間: "+s["mday"]+"\n")