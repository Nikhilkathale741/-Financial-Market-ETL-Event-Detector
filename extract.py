import yfinance as yf
from newsapi import NewsApiClient
from datetime import datetime, timedelta

def get_stock_data(ticker='AAPL', period='7d', interval='1h'):
    data = yf.download(ticker, period=period, interval=interval)
    return data.reset_index()

def get_news(company_name='Apple'):
    newsapi = NewsApiClient(api_key='5ec0177b13a448d2b5876f6a32907f27')
    date_from = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    articles = newsapi.get_everything(q=company_name, from_param=date_from, language='en')
    return articles['articles']
