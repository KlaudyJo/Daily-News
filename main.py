import json
import pandas as pd
import time
from news import Get_Current_News
from crypt import StocksCrypto
from weather import Weather_api

from send_email import EmailSent


file_path = 'text.txt'
def weather(file):
    weather = Weather_api()
    daily_temp, weather, weather_desc = weather.get_weather()
    with open(file) as file:
        text = file.read()
        text = text.replace("[temperature]", str(daily_temp))
        text = text.replace("[weather]", weather)
        text = text.replace("[description]", weather_desc)
    return text

def get_stocks():
    data_crypto = []
    data_stock = []
    
    f = open('stocks_crypto.json')
    stocks_crypto = json.load(f)
    crypto_symbols = [stocks_crypto['crypto'][i]['shortcut'] for i in range(len(stocks_crypto['crypto']))]
    stocks_symbols = [stocks_crypto['stocks'][i]['shortcut'] for i in range(len(stocks_crypto['stocks']))]

    stocksCrypto = StocksCrypto()
    for symbol in crypto_symbols:
        try:
            crypto = stocksCrypto.get_crypto((symbol))
            data_crypto.append(crypto)
            time.sleep(10)
        except:
            print(f"{symbol} is a problem!")

    for symbol in stocks_symbols:
        try:
            stock = stocksCrypto.get_stocks(symbol)
            
            data_stock.append(stock)
            time.sleep(15)
        except:
            print(f"{symbol} is a problem!")
    return data_crypto, data_stock

get_news = Get_Current_News()
news = get_news.get_news()
news_text =', \n'.join(news)
text = weather(file_path)
data_crypto, data_stock = get_stocks()
df = pd.DataFrame(data_crypto, columns=['Name', 'Close current day', 'Close previous day', 'Change'])
df2 = pd.DataFrame(data_stock, columns=['Name', 'Close current day', 'Close previous day', 'Change'])
sent = EmailSent()
sent.send_email(text,df,df2, news)
print('email sent')
