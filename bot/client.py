import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from bot.logging_config import setup_logger

logger = setup_logger(__name__)

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})

    def _sign(self, params: dict) -> str:
        query = urlencode(params)
        return hmac.new(self.secret_key.encode(), query.encode(), hashlib.sha256).hexdigest()

    def place_order(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        url = f"{BASE_URL}/fapi/v1/order"
        logger.debug(f"Request params: {params}")

        try:
            response = self.session.post(url, params=params)
            data = response.json()
            logger.debug(f"Response: {data}")

            if "code" in data and data["code"] != 200:
                logger.error(f"API Error: {data}")
                raise Exception(data.get("msg", "Unknown API error"))

            return data

        except requests.RequestException as e:
            logger.error(f"Network error: {e}")
            raise