"""
Helper utilities for the trading bot.
"""
from typing import Dict, Any, Optional
import os
from datetime import datetime
import logging
import pandas as pd


def setup_logging(log_level: str = 'INFO') -> None:
    """
    Set up logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('trading.log'),
            logging.StreamHandler()
        ]
    )


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from environment file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary containing configuration values
    """
    from dotenv import load_dotenv
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    load_dotenv(config_path)
    
    return {
        'API_KEY': os.getenv('API_KEY'),
        'SYMBOL': os.getenv('SYMBOL', 'BTC-USD'),
        'TIMEFRAME': os.getenv('TIMEFRAME', '1h'),
    }


def calculate_performance(data: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate trading performance metrics.
    
    Args:
        data: DataFrame with trading signals and price data
        
    Returns:
        Dictionary containing performance metrics
    """
    if 'Signal' not in data.columns:
        raise ValueError("Data must contain 'Signal' column")
    
    # Calculate returns
    data['Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
    
    # Calculate metrics
    total_return = (1 + data['Strategy_Returns']).prod() - 1
    sharpe_ratio = data['Strategy_Returns'].mean() / data['Strategy_Returns'].std() * (252 ** 0.5)
    
    return {
        'total_return': total_return,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': (data['Strategy_Returns'] + 1).cumprod().pipe(lambda x: (x.max() - x) / x.max()).max()
    }