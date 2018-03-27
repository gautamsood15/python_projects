import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text()
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            herf = 'https://buckysroom.org' + link.get("herf")
            title = link.string
           # print(herf)
           #  print(title)
            get_single_item_data(herf)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text()
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll("div", {"class":"i-name"}):
        print(item_name.string)
    for link in soup.findAll('a'):
        herf = "https://buckysroom.org" + link.get("herf")
        print(herf)


trade_spider(3)