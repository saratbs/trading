"""
Test trading strategies implementation.
"""
import pytest
import pandas as pd
import numpy as np
from src.strategies.strategy import MovingAverageCrossover


@pytest.fixture
def sample_data():
    """Create sample market data for testing."""
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    data = pd.DataFrame(
        data={
            'Open': np.random.randn(len(dates)).cumsum() + 100,
            'High': np.random.randn(len(dates)).cumsum() + 102,
            'Low': np.random.randn(len(dates)).cumsum() + 98,
            'Close': np.random.randn(len(dates)).cumsum() + 100,
            'Volume': np.random.randint(1000, 10000, len(dates))
        },
        index=dates
    )
    return data


def test_ma_crossover_strategy(sample_data):
    """Test Moving Average Crossover strategy."""
    # Initialize strategy
    strategy = MovingAverageCrossover(sample_data, short_window=10, long_window=20)
    
    # Calculate indicators
    strategy.calculate_indicators()
    
    # Check if indicators were calculated
    assert 'SMA_short' in strategy.data.columns
    assert 'SMA_long' in strategy.data.columns
    
    # Generate signals
    signals = strategy.generate_signals()
    
    # Check if signals were generated
    assert 'Signal' in signals.columns
    assert set(signals['Signal'].unique()).issubset({-1, 0, 1})  # Only valid signals