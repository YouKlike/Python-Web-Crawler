import urllib.request as req
import json
import matplotlib.pyplot as plt
src = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

with req.urlopen(src) as res:
    data = json.load(res)
    
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
AQI = []
SiteName = []

for exh in data['records']:
    if(exh['County']=='高雄市'):
        SiteName.append(exh['SiteName'])
        AQI.append(int(exh['AQI']))
        
plt.xlabel("高雄市各測站及時AQI")
plt.bar(SiteName , AQI)
plt.show()