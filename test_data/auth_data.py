import os

LOGIN_CASES = [
    ("emilys", "emilyspass", 200),
    ("emilys", "wrongpassword", 400),
]



USERNAME = os.getenv("API_USERNAME", "emilys")
PASSWORD = os.getenv("API_PASSWORD", "emilyspass")