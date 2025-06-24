import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from extract import get_stock_data, get_news
from transform import compute_volatility, clean_news
from aidetector import detect_anomalies

st.set_page_config(page_title="📈 Stock Anomaly Detector", layout="centered")

st.title("📊 Financial Market ETL + Event Detector")
st.caption("🔎 Track stock volatility and detect anomalies based on AI")

# --- User Input ---
ticker = st.text_input("Enter Stock Ticker Symbol (e.g. AAPL, TSLA, MSFT)", "AAPL")

if st.button("Run Analysis"):
    try:
        # Run pipeline
        stock_data = get_stock_data(ticker)
        stock_data = compute_volatility(stock_data)
        stock_data = detect_anomalies(stock_data)

        # Drop timezone
        stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], utc=True)
        stock_data['Datetime'] = stock_data['Datetime'].dt.tz_localize(None)

        # --- Plot ---
        st.subheader("📈 Volatility & Anomalies")

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(stock_data['Datetime'], stock_data['Volatility'], label='Volatility', color='blue')
        anomalies = stock_data[stock_data['anomaly'] == -1]
        ax.scatter(anomalies['Datetime'], anomalies['Volatility'], color='red', label='Anomalies', marker='x', s=100)
        ax.set_xlabel("Date")
        ax.set_ylabel("Volatility")
        ax.set_title(f"Volatility Plot for {ticker}")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # --- Download Button ---s
        st.subheader("📁 Download Stock Data")
        csv = stock_data.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download CSV", csv, file_name=f"{ticker}_stock_data.csv", mime='text/csv')

        # --- Footer ---
        st.markdown("---")
        st.markdown(
            "<div style='text-align: center;'>"
            "✨ Made with ❤️ by <strong>Nikhil Kathale</strong>"
            "</div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"🚨 Error: {str(e)}")
