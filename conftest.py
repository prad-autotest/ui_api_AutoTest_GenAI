import logging
import pytest
from utils.logging_config import setup_logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/test_run.log"),
            logging.StreamHandler()
        ]
    )

    @pytest.fixture(scope="session", autouse=True)
    def configure_logging():
        setup_logging()
