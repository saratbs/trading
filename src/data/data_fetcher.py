"""
Data fetcher module for retrieving market data.
"""
from typing import Optional, Dict, Any
import yfinance as yf
import pandas as pd


class DataFetcher:
    """
    A class to fetch market data from various sources.
    """
    
    def __init__(self, symbol: str):
        """
        Initialize the data fetcher.
        
        Args:
            symbol: The trading symbol to fetch data for
        """
        self.symbol = symbol
        self._ticker: Optional[yf.Ticker] = None
    
    def fetch_data(self, period: str = '1mo', interval: str = '1h') -> pd.DataFrame:
        """
        Fetch historical market data.
        
        Args:
            period: Time period to download data for (e.g., '1d', '1mo', '1y')
            interval: Data interval (e.g., '1m', '1h', '1d')
            
        Returns:
            DataFrame containing historical market data
        """
        self._ticker = yf.Ticker(self.symbol)
        return self._ticker.history(period=period, interval=interval)
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about the traded symbol.
        
        Returns:
            Dictionary containing symbol information
        """
        if not self._ticker:
            self._ticker = yf.Ticker(self.symbol)
        return self._ticker.info