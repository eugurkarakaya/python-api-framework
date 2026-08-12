from api.client import post, session,get

def login(username,password): #authanticated fixture gelmemeli. Login test edilmeden login fonksiyonunu çalıştırmış olurduk eğer fixture kullansaydık.
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