from bs4 import BeautifulSoup
import requests

url = 'https://www.ebay.com/sch/i.html?_nkw=graphics+card&_sacat=0&_from=R40&_trksid=p2334524.m570.l1313&_odkw=mewtwo+pokemon+card&_osacat=0'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
ebay_listing = soup.find_all("div", class_="s-item__info clearfix")

for item in ebay_listing:
    title = item.find("div", class_="s-item__title").text.strip()
    url = item.find("a", class_="s-item__link")["href"]
    price = item.find("span", class_="s-item__price").text

    print(title)
    print(url)
    print(price)