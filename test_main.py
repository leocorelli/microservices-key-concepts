from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_read_adder():
    response = client.get('add/2/2')
    assert response.status_code == 200
    assert response.json() == {"total": 4}

def test_read_subber():
    response = client.get('/sub/10/7')
    assert response.status_code == 200
    assert response.json() == {"total": 3}