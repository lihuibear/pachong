import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (windows NT 10.0; win64; x64)"}
content = requests.get("http://books.toscrape.com/",headers = headers).text
soup = BeautifulSoup(content,"html.parser")
all_prices = soup.findAll("p",attrs={"class":"price_color"})
for price in all_prices:
    print(price.string[2:])
all_bookname = soup.findAll("h3")
for title in all_bookname:
    all_links = title.find("a")
    print(all_links.string)





