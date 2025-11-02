from data.data_fetcher import DataFetcher
from strategies.strategy import TradingStrategy
from config import SYMBOL, TIMEFRAME

def main():
    # Initialize data fetcher
    fetcher = DataFetcher(SYMBOL)
    
    # Fetch market data
    data = fetcher.fetch_data(interval=TIMEFRAME)
    
    # Initialize and run strategy
    strategy = TradingStrategy(data)
    strategy.add_indicators()
    signals = strategy.generate_signals()
    
    # Print latest signals
    print(signals[['Close', 'RSI', 'MACD', 'Signal']].tail())

if __name__ == "__main__":
    main()