import requests
from bs4 import BeautifulSoup

url_wiki = 'https://en.wikipedia.org/wiki/The_Boat_That_Rocked'


def wiki_spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text()
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('div', {'class': 'noprint'}):
        herf = 'https://en.wikipedia.org' + link.get('herf')
        title = link.string
        sub_wiki_spider(herf)
        print(title)
        # print(herf)


def sub_wiki_spider(sub_url):
    source_code = requests.get(sub_url)
    plain_text = source_code.text()
    soup = BeautifulSoup(plain_text)
    for sub_item in soup.findAll('a', {'title': 'Radio Caroline'}):
        print(sub_item.string)
    for link in soup.findAll('a'):
        herf = "https://en.wikipedia.org" + link.get('herf')
        print(herf)


wiki_spider(url_wiki)
