import requests
import RegularExpression as RE
from bs4 import BeautifulSoup

def GetPrice(URL):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(BeautifulSoup(page.content, 'html.parser').prettify(), 'html.parser')
    name = soup.find(id='productTitle').get_text()
    priceStr = soup.find(id='priceblock_ourprice').get_text()
    convertedPrice = RE.ConvertPrice(price=priceStr)

    return name.strip(), convertedPrice
