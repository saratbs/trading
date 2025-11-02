"""
Trading strategy implementation.
"""
from typing import Optional
import pandas as pd
import numpy as np
import talib as ta


class TradingStrategy:
    """
    Base class for implementing trading strategies.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the trading strategy.
        
        Args:
            data: DataFrame containing market data
        """
        self.data = data
        self.signals: Optional[pd.DataFrame] = None
    
    def calculate_indicators(self) -> None:
        """
        Calculate technical indicators for the strategy.
        Should be implemented by child classes.
        """
        raise NotImplementedError("Subclasses must implement calculate_indicators()")
    
    def generate_signals(self) -> pd.DataFrame:
        """
        Generate trading signals based on indicators.
        Should be implemented by child classes.
        
        Returns:
            DataFrame containing trading signals
        """
        raise NotImplementedError("Subclasses must implement generate_signals()")


class MovingAverageCrossover(TradingStrategy):
    """
    Moving Average Crossover trading strategy.
    """
    
    def __init__(self, data: pd.DataFrame, short_window: int = 20, long_window: int = 50):
        """
        Initialize the MA Crossover strategy.
        
        Args:
            data: DataFrame containing market data
            short_window: Short-term moving average period
            long_window: Long-term moving average period
        """
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window
    
    def calculate_indicators(self) -> None:
        """Calculate short and long-term moving averages."""
        self.data['SMA_short'] = ta.SMA(self.data['Close'], timeperiod=self.short_window)
        self.data['SMA_long'] = ta.SMA(self.data['Close'], timeperiod=self.long_window)
    
    def generate_signals(self) -> pd.DataFrame:
        """
        Generate trading signals based on moving average crossovers.
        
        Returns:
            DataFrame with trading signals
        """
        if 'SMA_short' not in self.data.columns:
            self.calculate_indicators()
        
        self.data['Signal'] = 0
        # Buy signal when short MA crosses above long MA
        self.data.loc[self.data['SMA_short'] > self.data['SMA_long'], 'Signal'] = 1
        # Sell signal when short MA crosses below long MA
        self.data.loc[self.data['SMA_short'] < self.data['SMA_long'], 'Signal'] = -1
        
        return self.data