from api.client import get,post,put,delete

def test_get():
	response = get("/posts/1")
	assert response.status_code == 200

def test_create_post():
	payload = {
		"title": "API Test",
		"body": "Learning Python",
		"userId": 1
	}
	response = post("/posts/add",payload)

	assert response.status_code == 201
	data=response.json()
	assert data["title"]=="API Test"
	assert data["body"]=="Learning Python"

def test_put():
	payload = {
		"id": 1,
		"title": "Updated Title",
		"body": "Updated Body",
		"userId": 1
	}
	response=put("/posts/1",payload)
	data = response.json()
	assert response.status_code == 200
	assert data["title"]=="Updated Title"
	assert data["body"]=="Updated Body"
	assert data["userId"]==1

def test_delete_post():
    response = delete("/posts/1")
    assert response.status_code == 200