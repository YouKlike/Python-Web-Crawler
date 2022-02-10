import urllib.request as req
import json

src = 'https://data.taipei/api/v1/dataset/1f30d3ca-576b-4274-a1de-0f5ec0e32eaa?scope=resourceAquire'
with req.urlopen(src) as rsp:
    data = json.load(rsp)

mylist = data["result"]["results"]
for exh in mylist:
    
    print("單位:"+exh["租借單位"]+"\t車站："+exh["車站名稱"]+"\t活動名稱"+exh["活動名稱"]+"\t日期:"+exh["日期"]+"\n")