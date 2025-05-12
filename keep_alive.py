import requests
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('keep_alive.log'),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)
logger = logging.getLogger(__name__)

# URL of your Hugging Face Space
SPACE_URL = "https://umang0610-deepfake-detection.hf.space/health"

# Interval between requests (30 minutes = 1800 seconds)
PING_INTERVAL = 30 * 60

def ping_space():
    """Send an HTTP request to the Hugging Face Space to keep it alive."""
    try:
        response = requests.get(SPACE_URL, timeout=10)
        if response.status_code == 200:
            logger.info(f"Successfully pinged Space: {response.status_code}")
            logger.info(f"Response: {response.json()}")
        else:
            logger.warning(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error pinging Space: {str(e)}")

def main():
    logger.info("Starting keep-alive script for Hugging Face Space")
    while True:
        ping_space()
        logger.info(f"Sleeping for {PING_INTERVAL} seconds (30 minutes)")
        time.sleep(PING_INTERVAL)

if __name__ == "__main__":
    main()