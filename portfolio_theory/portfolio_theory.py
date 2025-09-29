import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# stocks we are going to handle
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'DB', 'AMZN']

# historical data - define start and end dates (using past dates with actual trading data)
start_date = '2025-01-01'
end_date = '2025-09-01'

def download_data():
    stock_dataframes = []
    stock_names = []
    
    for stock in stocks:
        data = yf.download(stock, start=start_date, end=end_date, auto_adjust=True)
        stock_dataframes.append(data['Close'])
        stock_names.append(stock)
                
    df = pd.concat(stock_dataframes, axis=1, keys=stock_names)
    df = df.dropna(how='all')
    
    return df

def main():
    stock_data = download_data()
    print("Stock Price Data:")
    print(stock_data.head())
    print(f"\nShape: {stock_data.shape}")
    print(f"Date range: {stock_data.index[0]} to {stock_data.index[-1]}")

if __name__ == "__main__":
    main()