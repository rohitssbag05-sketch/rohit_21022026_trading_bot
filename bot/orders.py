import logging

logger = logging.getLogger(__name__)


def execute_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    order_params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": float(quantity),
    }

    if order_type == "LIMIT":
        order_params["price"] = float(price)
        order_params["timeInForce"] = "GTC"

    current_price = client.get_symbol_price_ticker(symbol=symbol.upper()).get("price")

    if side == "SELL" and float(stop_price) >= current_price:
        raise ValueError("For SELL STOP, stop_price must be below current price.")

    if side == "BUY" and float(stop_price) <= current_price:
        raise ValueError("For BUY STOP, stop_price must be above current price.")

    if order_type == "STOP":
        order_params["price"] = float(price)
        order_params["stopPrice"] = float(stop_price)
        order_params["timeInForce"] = "GTC"

    logger.info(f"Order parameters constructed: {order_params}")

    response = client.place_order(**order_params)

    # ----- Handle different response structures -----

    if "algoId" in response:  # STOP / conditional orders
        formatted_response = {
            "orderId": response.get("algoId"),
            "status": response.get("algoStatus"),
            "executedQty": response.get("quantity"),
            "avgPrice": "N/A (Not triggered yet)",
            "type": response.get("orderType"),
        }
    else:  # MARKET / LIMIT
        formatted_response = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A"),
            "type": response.get("type"),
        }

    return formatted_response