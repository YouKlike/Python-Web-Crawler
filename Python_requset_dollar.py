#%%

import urllib.request as req
import json
import matplotlib.pyplot as plt

src = 'https://apiservice.mol.gov.tw/OdService/download/A17000000J-030185-NxT'

with req.urlopen(src) as res:
    data = json.load(res)
    
months = []
NTDmoney = []
CNDmoney = []
EUmoney = []
EAmoney = []

for exh in data:
    months.append(exh['年度'])
    NTDmoney.append(exh['新台幣'])
    CNDmoney.append(exh['人民幣'])
    EUmoney.append(exh['歐元'])
    EAmoney.append(exh['英鎊'])
    

for i in range(len(NTDmoney)):
    NTDmoney[i] = float(NTDmoney[i])
    CNDmoney[i] = float(CNDmoney[i])
    EUmoney[i] = float(EUmoney[i])
    EAmoney[i] = float(EAmoney[i])
    


plt.grid(True)
plt.figure(figsize=(20,20),dpi=100,linewidth = 2)
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
plt.title("2020兌換台幣的匯率")
plt.xlabel("月份")
plt.ylabel("匯率金額")
plt.plot(months , NTDmoney ,color = 'r')
plt.plot(months, CNDmoney , color= 'g')
plt.plot(months, EUmoney , color = 'c')
plt.plot(months , EAmoney , color = 'm')
plt.legend(['新台幣','人民幣','歐元','英鎊'])
plt.show()



#