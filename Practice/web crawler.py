import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_code = source_code.text()
        soup = BeautifulSoup(plain_code)
        for link in soup.findAll("a", {"class":"item-name"}):
            herf = "https://buckysroom.org" + link.get("herf")
            title = link.string
            print(herf)
        page += 1

trade_spider(1)