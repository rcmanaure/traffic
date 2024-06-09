import logging
import logging.config

import yaml

from src.config.settings import settings


def setup_logger():
    """Setup logger for the application"""
    # Load the YAML file
    with open("src/utils/log_conf.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Substitute environment variables
    config["loggers"]["uvicorn.error"]["level"] = settings.LOG_LEVEL

    config["loggers"]["uvicorn.access"]["level"] = settings.LOG_LEVEL

    # Configure logging
    logging.config.dictConfig(config)
    # Create logger to use in the app
    logger = logging.getLogger(__name__)
    return logger
