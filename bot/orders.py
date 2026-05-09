from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger(__name__)

def place_order(client: BinanceClient, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logger.info(f"Placing {order_type} {side} order | Symbol: {symbol} | Qty: {quantity} | Price: {price}")

    response = client.place_order(params)

    logger.info(f"Order placed successfully | OrderId: {response.get('orderId')} | Status: {response.get('status')}")

    return response