from fastapi import FastAPI, status
from pathlib import Path

from models.Data import Data 

import json
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# For a more robust application, consider moving configuration to a separate file or environment variables.
MOCKS_FILE = Path("./data/mocks.json")
# Using a lock to prevent race conditions when accessing the JSON file from concurrent requests.
file_lock = threading.Lock()

app = FastAPI(
    title="Mock Data API",
    description="An API to get and post mock data, stored in a JSON file.",
    version="1.0.0",
)

def _load_mocks_unsafe() -> dict:
    """
    Loads mock data from the JSON file without acquiring a lock.
    Assumes the file exists.
    """
    try:
        content = MOCKS_FILE.read_text()
        if not content:
            return {}
        return json.loads(content)
    except json.JSONDecodeError:
        logger.error(f"Could not decode JSON from {MOCKS_FILE}. Returning empty dict.")
        return {}

def _save_mocks_unsafe(data: dict):
    """Saves mock data to the JSON file without acquiring a lock."""
    MOCKS_FILE.write_text(json.dumps(data, indent=4))

@app.on_event("startup")
def on_startup():
    """Ensure the mocks file exists on startup."""
    with file_lock:
        if not MOCKS_FILE.exists():
            logger.info(f"Mocks file not found. Creating a new one at {MOCKS_FILE}")
            _save_mocks_unsafe({})

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint providing a simple status."""
    return {"status": "healthy"}

@app.get("/data", response_model=Data, tags=["Data"])
async def get_data():
    """Retrieve all mock data."""
    with file_lock:
        return _load_mocks_unsafe()

@app.post("/data", status_code=status.HTTP_200_OK)
async def update_data():
    """Update or create a data entry."""
    with file_lock:
        mocks = _load_mocks_unsafe()
        test= "Hola"
        mocks[test] = test
        _save_mocks_unsafe(mocks)
    return {"message": "Data updated successfully", "data": test}
