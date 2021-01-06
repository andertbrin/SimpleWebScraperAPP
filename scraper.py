import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/DualSense-Wireless-Controller-PlayStation-5/dp/B08FC6C75Y/\
    ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=\
        03b28c2c-71e9-4947-aa06-f8b5dc8bf880&pf_rd_r=EGSY9N1FXJMD2SPKYTTH&pf_rd_s=\
            merchandised-search-3&pf_rd_t=101&qid=1489016289&rnid=16225016011&s=videogames-intl-ship&sr=1-1'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ AppleWebKit/537.36\ \
    (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    conv_price = float(price[1:])
    print(conv_price)

check_price()
