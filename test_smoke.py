import requests

def test_home_endpoint():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.text == "Hello, Smoke Test!"

def test_status_endpoint():
    response = requests.get("http://localhost:5000/status")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
