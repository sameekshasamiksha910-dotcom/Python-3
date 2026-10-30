
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)

logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error occurred")
logging.critical("Critical error detected")

print("Logging demonstration completed.")
