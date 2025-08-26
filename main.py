from pathlib import Path

import sys
import logging

from src.app import app
from src.config.Base import settings
ROOT_DIR = Path(__file__).resolve().parent

sys.path.append(str(ROOT_DIR))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Starting the FastAPI application...")
logger.info(f"Project root directory: {ROOT_DIR}")
logger.info(f"Running on Python {sys.version}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
