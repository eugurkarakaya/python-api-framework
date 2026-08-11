import os

BASE_URL = os.getenv("BASE_URL", "https://dummyjson.com")
TIMEOUT = float(os.getenv("TIMEOUT", "10"))
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}

USERNAME=os.getenv("API_USERNAME","emilys")
PASSWORD=os.getenv("API_PASSWORD","emilyspass")