# Binance Futures Testnet Trading Bot

A CLI-based Python trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Setup

1. Clone the repository
2. Install dependencies:
```bash
   pip3 install -r requirements.txt
```
3. Create a `.env` file in the root directory:
    API_KEY=your_api_key_here
    SECRET_KEY=your_secret_key_here

## How to Run

### Market Order
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
```bash
python3 cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 75000
```

### SELL Order
```bash
python3 cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

## Project Structure

trading_bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading_bot.log
├── cli.py
├── .env
└── requirements.txt

## Assumptions
- Only USDT-M Futures Testnet is supported
- Testnet base URL: https://testnet.binancefuture.com
- LIMIT orders require a price argument