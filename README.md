# Binance Futures Testnet Trading Bot

A structured Python CLI application for placing orders on Binance USDT-M Futures Testnet.

This project demonstrates clean architecture, input validation, logging, and error handling while interacting with the Binance Futures Testnet API.

---

## 🚀 Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Place **STOP (Stop-Limit / Conditional)** orders (Bonus)
- Supports both **BUY** and **SELL**
- CLI-based user input
- Structured modular architecture
- Input validation before API calls
- Exchange rule validation (minimum notional)
- Detailed logging to file
- Exception handling for API and network errors

---

## 🏗 Project Structure


trading_bot/
│
├── bot/
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order execution logic
│ ├── validators.py # Input and exchange validation
│ └── logging_config.py
│
├── logs/
│ └── trading.log
│
├── cli.py # CLI entry point
├── .env # API credentials (not committed)
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository


git clone <your-repo-url>
cd trading_bot


### 2️⃣ Create Virtual Environment


python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows


### 3️⃣ Install Dependencies


pip install -r requirements.txt


### 4️⃣ Create `.env` File

Create a `.env` file in the root directory:


BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret


> API keys must be generated from:  
> https://testnet.binancefuture.com

Ensure:
- Futures trading permission enabled
- No IP restriction (for testing)

---

## ▶️ How to Run

### MARKET Order


python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


---

### LIMIT Order


python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000


---

### STOP (Conditional) Order (Bonus)


python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.002 --price 63000 --stop_price 64000


---

## 📋 Example Output


===== ORDER REQUEST =====
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.002
Price: 70000

===== ORDER RESPONSE =====
Order ID: 123456789
Status: NEW
Executed Qty: 0.000
Avg Price: N/A

✅ Order executed successfully


---

## 📝 Logging

All API requests, responses, and errors are logged to:


logs/trading.log


Logging includes:
- Order parameters
- Raw exchange response
- API errors
- Unexpected exceptions

---

## 🧠 Design Decisions

- Separation of concerns (CLI / Business Logic / Client)
- Centralized logging configuration
- Validation before API calls
- Exchange rule validation (minimum notional requirement)
- Clean and extensible structure for adding new order types

---

## ⚠️ Assumptions

- USDT-M Futures only
- Binance Futures Testnet only
- Cross margin mode (default)
- Leverage not explicitly configured

---

## 📦 Dependencies

- python-binance
- python-dotenv

---

## ✅ Bonus Implemented

- Added STOP (Stop-Limit / Conditional) order support
- Extended validation for conditional orders
- Handled different response structures (standard vs conditional orders)

---

## 📧 Submission

Includes:
- Source code
- README
- requirements.txt
- Log files demonstrating:
  - One MARKET order
  - One LIMIT order
  - One STOP order (bonus)

---