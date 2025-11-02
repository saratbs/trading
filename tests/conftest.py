"""
PyTest Configuration
Setup test fixtures and common test utilities.
"""

import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    """Provide sample market data for testing."""
    return pd.DataFrame()