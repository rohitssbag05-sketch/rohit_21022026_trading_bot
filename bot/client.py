import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv


load_dotenv()

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise EnvironmentError("API credentials not found in environment variables.")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized.")

    def get_mark_price(self, symbol):
        data = self.client.futures_mark_price(symbol=symbol)
        return float(data["markPrice"])

    def place_order(self, **kwargs):
        try:
            
            logger.info(f"Sending order to Binance: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Received response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Binance request error: {str(e)}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise