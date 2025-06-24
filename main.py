from extract import get_stock_data, get_news
from transform import compute_volatility, clean_news
from load import load_to_postgres
from aidetector import detect_anomalies

def run_pipeline():
    print(" [STEP 1] Fetching stock data...")
    stock_data = get_stock_data('AAPL')
    print(stock_data.head())

    print("[STEP 2] Computing volatility...")
    stock_data = compute_volatility(stock_data)
    print(stock_data[['Close', 'Return', 'Volatility']].tail())

    print("Columns available:", stock_data.columns)
    print(stock_data.tail())
    print("DEBUG Columns Before Anomaly Detection:", stock_data.columns.tolist())



    print(" [STEP 3] Detecting anomalies...")
    stock_data = detect_anomalies(stock_data)
    print(stock_data[['Volatility', 'anomaly']].tail())

    print(" [STEP 4] Fetching news...")
    news = get_news('Apple')
    news_df = clean_news(news)
    print(news_df.head())

    print(" [STEP 5] Loading to csv")
    stock_data.to_csv("stock_data.csv", index=False)
    news_df.to_csv("news_data.csv", index=False)
    print("💾 Data saved to CSVs successfully.")


    print(" Done! All data loaded successfully.")

if __name__ == "__main__":
    run_pipeline()
