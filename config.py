import os

BASE_URL = os.getenv("BASE_URL", "https://dummyjson.com")
TIMEOUT = float(os.getenv("TIMEOUT", "10"))
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}
