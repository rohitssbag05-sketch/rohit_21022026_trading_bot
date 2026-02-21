# Binance Futures Testnet Trading Bot

A structured Python CLI application for placing orders on Binance USDT-M Futures Testnet.

This project demonstrates clean architecture, input validation, structured logging, and robust error handling while interacting with the Binance Futures Testnet API.

---

## 🚀 Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Place **STOP (Stop-Limit / Conditional)** orders (Bonus)
- Supports both **BUY** and **SELL**
- CLI-based user input
- Exchange rule validation (minimum notional check)
- Structured modular architecture
- Centralized logging of API requests and responses
- Graceful exception handling

---

## 🏗 Project Structure


trading_bot/
├── bot/
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Order execution logic
│ ├── validators.py # Input + exchange validation
│ └── logging_config.py # Logging configuration
├── logs/
│ └── trading.log # Execution logs
├── cli.py # CLI entry point
├── .env # API credentials (not committed)
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
2️⃣ Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create .env File

Create a .env file in the root directory:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret

⚠️ API keys must be generated from:

https://testnet.binancefuture.com

Ensure:

Futures trading permission is enabled

No IP restrictions (for testing)

▶️ Usage Examples
✅ MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
✅ LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
✅ STOP (Conditional) Order (Bonus)
python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.002 --price 63000 --stop_price 64000

Explanation:

stop_price = trigger price

price = limit price placed after trigger

📋 Example Outputs
MARKET / LIMIT Response
===== ORDER REQUEST =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

===== ORDER RESPONSE =====
Order ID: 123456789
Status: FILLED
Executed Qty: 0.002
Avg Price: 65432.10

✅ Order executed successfully
STOP (Conditional) Response
===== ORDER REQUEST =====
Symbol: BTCUSDT
Side: SELL
Type: STOP
Quantity: 0.002
Price: 63000
Stop Price: 64000

===== ORDER RESPONSE =====
Order ID: 1000000015704255
Status: NEW
Executed Qty: 0.002
Avg Price: N/A (Not triggered yet)

✅ Order executed successfully

Note:
STOP orders return algoId and algoStatus instead of standard orderId and status.
The application handles both response structures appropriately.

📝 Logging

All API interactions are logged to:

logs/trading.log

Logs include:

Order parameters sent to Binance

Raw API responses

API errors

Unexpected exceptions

Log format:

Timestamp | Level | Logger | Message
🧠 Design Decisions

Clear separation of concerns:

CLI Layer

Business Logic Layer

API Client Layer

Validation before API calls

Exchange minimum notional validation (>= 100 USDT)

Structured logging for debugging and traceability

Extensible architecture for adding new order types

⚠️ Assumptions

USDT-M Futures only

Binance Futures Testnet only

Default margin mode

Leverage not explicitly configured

Minimum notional requirement enforced (>= 100 USDT)

📦 Dependencies

python-binance

python-dotenv

Install via:

pip install -r requirements.txt
