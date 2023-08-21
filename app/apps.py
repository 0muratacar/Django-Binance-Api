from django.apps import AppConfig
from env_config import api_key, api_secret
from binance.client import Client
import logging
from django.conf import settings


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        try:
            client = Client(api_key, api_secret)
            settings.BINANCE_CLIENT = client

            logging.info("Connected to Binance API successfully.")
        except Exception as e:
            logging.error(f"An error occurred when connecting to Binance: {e}")
