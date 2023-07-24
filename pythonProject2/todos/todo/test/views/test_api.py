import pytest

def test_get_posts(client, test_data):
    response = client.get("/api/todo/")
    assert response.status_code == 200
    assert len(response.json()['todo']) == 5
    assert response.json()['todo'][0]['username'] == 'lena'


