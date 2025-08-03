import sys
from pathlib import Path
import logging

# Add project root to the Python path to allow absolute imports.
ROOT_DIR = Path(__file__).resolve().parent

sys.path.append(str(ROOT_DIR))


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting the FastAPI application...")
logger.info(f"Project root directory: {ROOT_DIR}")
logger.info(f"Running on Python {sys.version}")

from src.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
