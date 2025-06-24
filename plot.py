import pandas as pd
import matplotlib.pyplot as plt

# Load stock data
df = pd.read_csv("stock_data.csv")

# Convert 'Datetime' to datetime type and remove timezone
if 'Datetime' in df.columns:
    df['Datetime'] = pd.to_datetime(df['Datetime'], utc=True)
    df['Datetime'] = df['Datetime'].dt.tz_localize(None)  # <-- this line fixes the issue

# Plot Volatility and Anomalies
plt.figure(figsize=(12, 6))
plt.plot(df['Datetime'], df['Volatility'], label='Volatility', color='blue')

# Check if anomaly column exists
if 'anomaly' in df.columns:
    plt.scatter(
        df[df['anomaly'] == -1]['Datetime'],
        df[df['anomaly'] == -1]['Volatility'],
        color='red', label='Anomaly', marker='x', s=100
    )

plt.title("📉 Stock Volatility & Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
