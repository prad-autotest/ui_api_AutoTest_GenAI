import logging
import os
from datetime import datetime

def setup_logging(log_dir="logs"):
    """
    Configures global logging settings.
    Logs are written to both console and file.
    """

    # Ensure logs directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Timestamped log file
    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    # Basic configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode='w'),
            logging.StreamHandler()
        ]
    )

    logging.getLogger().info("Logging is configured.")
