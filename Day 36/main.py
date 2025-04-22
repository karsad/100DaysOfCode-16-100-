import os
import requests
from twilio.rest import Client
import stock

STOCK = "NOKIA.PAR"
COMPANY_NAME = "Nokia Oyj"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_MY_API_KEY = os.environ.get("STOCK_MY_API_KEY")
STOCK_OPTIONS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_MY_API_KEY
}
NEWS_OPTIONS = {
    "function": "NEWS_SENTIMENT",
    "tickers": "NOK",
    "apikey": STOCK_MY_API_KEY
}

def get_stock():
    print(STOCK_OPTIONS)
    response = requests.get(STOCK_URL, STOCK_OPTIONS)
    response.raise_for_status()
    return response.json()

def get_news():
    response = requests.get(STOCK_URL, NEWS_OPTIONS)
    response.raise_for_status()
    return response.json()

def send_sms(message: str):
    client = Client(os.environ.get("ACC_SID"), os.environ.get("ACC_TOKEN"))
    message = client.messages.create(
    from_='+19787055741',
    body = 'asdf',
    to = os.environ.get("MY_PHONE")
    )
    print(message.sid)


nokia = get_stock()
stock_data = nokia['Time Series (Daily)']

days = list(stock_data.keys())
stock_last_day = stock_data[days[0]]
stock_day_before = stock_data[days[1]]

stock_last_day_close_price = float(stock_last_day['4. close'])
stock_day_before_close_price = float(stock_day_before['4. close'])

percent_change = (stock_last_day_close_price  - stock_day_before_close_price) / stock_last_day_close_price  * 100

news = get_news()

if percent_change >= 0:
    msg = f"{COMPANY_NAME} {percent_change:.2f}▲\nHeadline: {news['feed'][0]['title']}\nBrief:{news['feed'][0]['summary']}"
else:
    msg = f"{COMPANY_NAME} {percent_change:.2f}▼\nHeadline: {news['feed'][0]['title']}\nBrief:{news['feed'][0]['summary']}"

send_sms(msg)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

