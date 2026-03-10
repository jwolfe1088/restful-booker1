import requests

def test_ping(base_url):
    response = requests.get(f"{base_url}/ping")
    assert response.status_code == 201