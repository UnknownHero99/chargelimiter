import logging, sys

logger = logging.getLogger("chargingLimit")
loglevel = "INFO"
log_level = "DEBUG"
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.setLevel(log_level)
logger.addHandler(log_handler)