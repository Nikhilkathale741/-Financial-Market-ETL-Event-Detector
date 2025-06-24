from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    df = df.copy()
    
    # Find column name containing 'Volatility' in case it's renamed or prefixed
    vol_col = next((col for col in df.columns if 'Volatility' in col), None)
    
    if vol_col is None:
        raise ValueError("No column containing 'Volatility' found in DataFrame.")

    df = df.dropna(subset=[vol_col])

    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[[vol_col]])

    return df
