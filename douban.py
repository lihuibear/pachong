import requests
from bs4 import BeautifulSoup
import pandas as pd
titles = []
stars = []
inqs = []
headers = {"User-Agent": "Mozilla/5.0 (windows NT 10.0; win64; x64)"}
for start_num in range(0,250,25):
    response = requests.get(f"http://movie.douban.com/top250?start={start_num}",headers = headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_title = soup.findAll("span",attrs={"class":"title"})
    all_star = soup.findAll("span",attrs={"class":"rating_num"})
    all_inq = soup.findAll("span",attrs={"class":"inq"})
    for title,star,inq in zip(all_title,all_star,all_inq):
        title_string = title.string
        star_string = star.string
        inq_string = inq.string
        if "/" not in title_string:
            # print(title_string)
            # print(star_string)
            # print(inq_string)
            titles.append(title_string)
            stars.append(star_string)
            inqs.append(inq_string)


    data = {"Title": titles, "Rating": stars,"inq":inqs}
    df = pd.DataFrame(data)

    df.to_excel("movies.xlsx", index=False)

