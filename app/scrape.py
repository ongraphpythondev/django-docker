import requests
from bs4 import BeautifulSoup

def href_scrape(url):
    a = []
    data = requests.get(url)
    img_url = url
    s = BeautifulSoup(data.text , "html.parser")
    for i in s.find_all('a'):
        href = i.attrs['href']
        if href.startswith("/"):
            url += href
            if url not in a :
                a.append(url)
    return a


def img_scrape(url):
    img = []
    data = requests.get(url)
    img_url = url
    s = BeautifulSoup(data.text , "html.parser")
    for i in s.find_all('img'):
        src = i.attrs['src']
        img.append(src)
    return img