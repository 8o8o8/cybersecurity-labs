import requests
import pandas as pd

def fetch_sol_prices(days=30):
    url = f"https://api.coingecko.com/api/v3/coins/solana/market_chart"
    params = {"vs_currency": "usd", "days": days}
    response = requests.get(url, params=params)
    data = response.json()
    prices = [price[1] for price in data["prices"]]
    dates = [pd.to_datetime(price[0], unit='ms') for price in data["prices"]]
    df = pd.DataFrame({"date": dates, "price": prices})
    return df

def calculate_moving_averages(df):
    df["7d_ma"] = df["price"].rolling(window=7).mean()
    df["14d_ma"] = df["price"].rolling(window=14).mean()
    return df

if __name__ == "__main__":
    df = fetch_sol_prices()
    df = calculate_moving_averages(df)
    latest = df.iloc[-1]
    print(f"Date: {latest['date'].date()}")
    print(f"Current Price: ${latest['price']:.2f}")
    print(f"7-Day MA: ${latest['7d_ma']:.2f}")
    print(f"14-Day MA: ${latest['14d_ma']:.2f}")