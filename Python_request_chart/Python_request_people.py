import urllib.request,csv
import matplotlib.pyplot as plt

url = 'https://gis.taiwan.net.tw/od/01_PRD/%E6%AD%B7%E5%B9%B4%E5%9C%8B%E5%85%A7%E4%B8%BB%E8%A6%81%E8%A7%80%E5%85%89%E9%81%8A%E6%86%A9%E6%93%9A%E9%BB%9E%E9%81%8A%E5%AE%A2%E4%BA%BA%E6%95%B8%E6%9C%88%E5%88%A5%E7%B5%B1%E8%A8%88.csv'

webpage = urllib.request.urlopen(url)
data = csv.reader(webpage.read().decode('UTF-8').splitlines())
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

people = []
months = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in data:
    if (i[0] in '2020' and i[3] in '莒光樓'):
        for a in range(5,17):
            people.append(int(i[a]))
        
for i in range(len(people)):
    print(people[i])


plt.bar(months, people)
plt.xlabel('月份')
plt.ylabel('人數')
plt.show()