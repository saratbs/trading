import pandas as pd
import ta

class TradingStrategy:
    def __init__(self, data):
        self.data = data
    
    def add_indicators(self):
        # Add RSI
        self.data['RSI'] = ta.momentum.RSIIndicator(self.data['Close']).rsi()
        # Add MACD
        macd = ta.trend.MACD(self.data['Close'])
        self.data['MACD'] = macd.macd()
        self.data['MACD_Signal'] = macd.macd_signal()
        
    def generate_signals(self):
        self.data['Signal'] = 0
        # Buy signal: RSI < 30 and MACD > Signal
        self.data.loc[(self.data['RSI'] < 30) & 
                      (self.data['MACD'] > self.data['MACD_Signal']), 'Signal'] = 1
        # Sell signal: RSI > 70 and MACD < Signal
        self.data.loc[(self.data['RSI'] > 70) & 
                      (self.data['MACD'] < self.data['MACD_Signal']), 'Signal'] = -1
        return self.data