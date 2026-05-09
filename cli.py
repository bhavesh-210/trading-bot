import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, default=None, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)

        client = BinanceClient(
            api_key=os.getenv("API_KEY"),
            secret_key=os.getenv("SECRET_KEY")
        )

        print(f"\n--- Order Request ---")
        print(f"Symbol   : {args.symbol.upper()}")
        print(f"Side     : {args.side.upper()}")
        print(f"Type     : {args.order_type.upper()}")
        print(f"Quantity : {args.quantity}")
        if args.price:
            print(f"Price    : {args.price}")

        response = place_order(client, args.symbol, args.side, args.order_type, args.quantity, args.price)

        print(f"\n--- Order Response ---")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")
        print(f"\n✅ Order placed successfully!")

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"\n❌ Validation Error: {e}")

    except Exception as e:
        logger.error(f"Order failed: {e}")
        print(f"\n❌ Order Failed: {e}")

if __name__ == "__main__":
    main()