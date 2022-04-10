# -*- coding: utf8 -*-
import time
import random
import requests
from bs4 import BeautifulSoup
import json
import csv

url = "insert a link to the wildberries store"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}
req = requests.get(url)
src = req.text
# print(src)
# with open ("index.html", "w", encoding="UTF-8-sig") as file:
#     file.write(src.replace('\u20bd', 'rubl'))

with open("index.html", encoding="utf-8-sig") as file:
   src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_goods = soup.find_all(class_='product-card__main')

for item in all_goods:
    item_text=item.text
    itemhref =("https://www.wildberries.ru" + item.get("href"))
    names = (item.select_one("span.goods-name").text)
    price = (item.find("span", class_="price-old-block").find("del").text)
    print(itemhref, names, price)

    p_info = []
    p_info.append(
        {
            "Names": names,
            "Price": price,
            "href": itemhref
        }
    )
    print((p_info))
    with open("test.json", "a", encoding="utf-8-sig") as file:
         json.dump(p_info, file, indent=4, ensure_ascii=False)

    with open("test.csv", "a", newline='', encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
        (
            names,
            price,
            itemhref
        )
    )
