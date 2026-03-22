import requests

def test_ping(api_base_url):
    response = requests.get(f"{api_base_url}/ping")
    assert response.status_code == 201