import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
STOCK_KEY = os.environ.get(ALPHA_VANTAGE_STOCK_KEY)
TWILIO_SID = os.environ.get(TWILIO_SID)
TWILIO_AUTH_TOKEN = os.environ.get(TWILIO_AUTH_TOKEN)
COMPANY_NAME = "Tesla Inc"
NEWS_KEY = os.environ.get(NEWS_API_KEY)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}
news_params = {
    "apiKey": NEWS_KEY,
    "qInTitle": COMPANY_NAME

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
stock_details = [detail for date,detail in stock_data["Time Series (Daily)"].items()]
stock_price_yesterday = float(stock_details[0]["4. close"])
stock_price_BeforeYesterday = float(stock_details[1]["4. close"])
price_change = stock_price_yesterday - stock_price_BeforeYesterday
percent_change = (price_change / stock_price_yesterday) * 100
if abs(percent_change) > 0.1:
    if percent_change < 0:
        p1 = f"{STOCK_NAME}: 🔻{abs(percent_change):.1f}%"
    else:
        p1 = f"{STOCK_NAME}: 🔺{abs(percent_change):.1f}%"

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_articles = [article for article in news_data["articles"]]
    articles_filt = news_articles[:3]
    msg_list = [f"Headline: {article['title']}.\nBrief: {article['description']}." for article in articles_filt]

    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    for message in msg_list:
        client.messages.create(
            body=f"{p1}\n {message}",
            from_=os.environ.get(FROM_NUMBER),
            to="<your ph num>",
        )

