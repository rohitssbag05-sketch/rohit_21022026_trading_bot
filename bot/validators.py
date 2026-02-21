MIN_NOTIONAL = 100  # Binance Futures Testnet rule


def validate_order_input(symbol, side, order_type, quantity, price, stop_price):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL.")

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP.")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        raise ValueError("Quantity must be a valid positive number.")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

    if order_type == "STOP":
        if price is None or stop_price is None:
            raise ValueError("Both price and stop_price are required for STOP orders.")

    # Notional validation (for LIMIT and STOP)
    if order_type in ["LIMIT", "STOP"] and price is not None:
        notional = float(quantity) * float(price)
        if notional < MIN_NOTIONAL:
            raise ValueError(
                f"Order notional must be >= {MIN_NOTIONAL} USDT. "
                f"Current notional: {notional}"
            )

    return True