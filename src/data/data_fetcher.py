import yfinance as yf
import pandas as pd

class DataFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def fetch_data(self, period='1mo', interval='1h'):
        ticker = yf.Ticker(self.symbol)
        df = ticker.history(period=period, interval=interval)
        return df