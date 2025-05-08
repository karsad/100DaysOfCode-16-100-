import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
URL2 = "https://appbrewery.github.io/instant_pot/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}
TARGET_PRICE = 100

response = requests.get(URL, headers=HEADER)
soup = BeautifulSoup(response.text, "html.parser")
price = float((soup.find(class_="a-price-whole").getText() + soup.find(class_="a-price-fraction").getText()).replace(",", "."))
print(price)

if price <= TARGET_PRICE:
    print(f"Current price is lower than {TARGET_PRICE}$!")