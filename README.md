# 📈 Financial Market ETL + Stock Event Detector

A powerful mini-project built with Python, Streamlit, and AI to track stock price volatility and detect unusual market behavior using anomaly detection techniques!

> ✨ Made with ❤️ by **Nikhil Kathale**

---

## 🚀 Features

- ✅ **Extract stock data** using Yahoo Finance API
- 📰 **Scrape related news headlines** using Google News
- ⚙️ **ETL pipeline** to clean, transform, and load data
- 📉 **Calculate volatility**
- 🤖 **AI-based anomaly detection** using Isolation Forest
- 🎛️ **Interactive Streamlit UI** to enter stock tickers and view results
- 📊 **Visualizations** of volatility and anomalies
- 📥 **Download CSV** functionality
- 🛢️ **Load data to PostgreSQL** with SQLAlchemy

---

## 📸 Demo Screenshot

![image](https://github.com/user-attachments/assets/341c3e4d-0eb0-47f3-9587-0bb3e0b3823c)


---

## 🧪 Tech Stack

- Python 3
- Pandas, Matplotlib
- Streamlit
- Scikit-learn (Isolation Forest)
- SQLAlchemy + PostgreSQL
- yfinance & Google News APIs

---

## 🧰 How to Run

```bash
# Clone the repo
git clone https://github.com/Nikhilkathale741/-Financial-Market-ETL-Event-Detector.git
cd Financial-Market-ETL-Event-Detector

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # on Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
