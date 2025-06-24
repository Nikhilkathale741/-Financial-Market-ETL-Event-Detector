import pandas as pd
import numpy as np

def compute_volatility(df):
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Return'].rolling(window=5).std()
    return df

def clean_news(news_articles):
    return pd.DataFrame([{
        'title': article['title'],
        'publishedAt': article['publishedAt'],
        'source': article['source']['name']
    } for article in news_articles])
