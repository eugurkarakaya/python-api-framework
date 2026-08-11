import requests
import logging
import time
from config import BASE_URL,TIMEOUT,DEFAULT_HEADERS

session = requests.Session()
logger=logging.getLogger(__name__)

def build_url(endpoint):
    return f"{BASE_URL}{endpoint}"

def send_request(method, endpoint, **kwargs):

    headers = DEFAULT_HEADERS.copy()
    headers.update(kwargs.pop("headers", {}))
    timeout= kwargs.pop("timeout",TIMEOUT) #Eğer kullanıcı bu request için timeout verdiyse onu kullan, vermediyse config'deki TIMEOUT değerini kullan.

    url = build_url(endpoint)

    logger.info(f"{method} {url}")

    start = time.perf_counter()

    try:
        response = session.request(
            method=method,
            url=url,
            timeout=timeout,
            headers=headers,
            **kwargs
        )
    except requests.exceptions.Timeout:
        logger.error(f"{method}{url} -> TIMEOUT")
        raise

    end = time.perf_counter()
    duration = end - start

    if response.status_code >= 500:
        logger.error(
            f"{method} {url} -> {response.status_code} ({duration:.3f}s)"
        )
    elif response.status_code >= 400:
        logger.warning(
            f"{method} {url} -> {response.status_code} ({duration:.3f}s)"
        )
    else:
        logger.info(
            f"{method} {url} -> {response.status_code} ({duration:.3f}s)"
        )
    return response


def login(username,password):
    payload = {
        "username":username,
        "password":password
    }
    response=post("/auth/login", payload)
    if response.status_code == 200:
        data = response.json()
        session.headers.update({
            "Authorization": f"Bearer {data['accessToken']}"
        })

    return response

def me():
    return get("/auth/me")

def get(endpoint,**kwargs):
    return send_request("GET",endpoint,**kwargs)

def post(endpoint,data):
    return send_request("POST",endpoint,json=data)

def put(endpoint, data):
    return send_request("PUT",endpoint,json=data)

def delete(endpoint):
    return send_request("DELETE",endpoint)