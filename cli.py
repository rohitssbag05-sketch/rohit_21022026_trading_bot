import argparse
import logging

from bot.client import BinanceFuturesClient
from bot.orders import execute_order
from bot.validators import validate_order_input
from bot.logging_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP"])
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    parser.add_argument("--stop_price")
    args = parser.parse_args()

    try:
        validate_order_input(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price,
    args.stop_price
)

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.type in ["LIMIT", "STOP"]:
         print(f"Price: {args.price}")

        if args.type == "STOP":
            print(f"Stop Price: {args.stop_price}")
        client = BinanceFuturesClient()

        response = execute_order(
    client,
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price,
    args.stop_price
)

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")
        print(f"Avg Price: {response['avgPrice']}")
        print("\n✅ Order executed successfully")

    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        print(f"\n❌ Order failed: {str(e)}")


if __name__ == "__main__":
    main()