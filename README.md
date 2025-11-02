# Trading Bot Project

## Development Guidelines

### Code Formatting
- All code contributions should follow the formatting guidelines in `.github/copilot/instructions.md`
- Use four backticks for code blocks
- Include language identifier and filepath where applicable
- Mark existing code with comments

### Project Structure
```
trading/
├── src/
│   ├── __init__.
|   |── config.py
│   ├── data/
│   │   └── __init__.py
|   |   └── data_fetcher.py
│   ├── strategies/
│   │   └── __init__.py
|   |   └── strategy.py
│   └── utils/
│       └── __init__.py
|       └── helpers.py
├── tests/
│   └── conftest.py
|   └── test_strategy.py
├── docs/
└── requirements.txt
```

### Getting Started
1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Follow coding guidelines