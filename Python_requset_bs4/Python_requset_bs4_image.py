'''
輸入關鍵字從網站中下載輸入關鍵字的圖片
'''

import requests
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
 
keyword = input("請輸入要下載的圖片: ")
html = requests.get(f"https://wall.alphacoders.com/search.php?search={keyword}")
sp = BeautifulSoup(html.text , 'html.parser')
results = sp.find_all("img",{"class":"img-responsive"},limit=5)
image_links=[]

for result in results:
    image_links.append(result.get("src"))
    
if not os.path.exists("images"): 
    os.mkdir("images")
    
for i in range(len(image_links)): 
    img=requests.get(image_links[i])

    with open("images\\" + keyword + str(i+1) + ".jpg", "wb") as file: 
        file.write(img.content) 
        image = Image.open("images\\" + keyword + str(i+1) + ".jpg")
        plt.imshow(image)
        plt.show()