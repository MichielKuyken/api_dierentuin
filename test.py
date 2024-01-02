import requests
import json


def test_post_eigenaar():
    response = requests.post('http://127.0.0.1:8000/eigenaar/',
                             json={"id": 1, "voornaam": "Michiel", "achternaam": "Kuyken", "email": "test", "password": "wachtwoord"})
    assert response.status_code == 200
    assert response.json() == "Eigenaar successfully created!"


def test_post_access_token():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    request_data = {
        "client_id": "",
        "client_secret": "",
        "scope": "",
        "grant_type": "",
        "refresh_token": "",
        "username": "test",
        "password": "wachtwoord"
    }
    response = requests.post('http://127.0.0.1:8000/token',
                             data=request_data,
                             headers=headers)
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    return access_token




def test_post_manager():
    response = requests.post('http://127.0.0.1:8000/managers/',
                             json={"id": 1, "voornaam": "Michiel", "achternaam": "Kuyken", "manager_nummer": "M01", "foto": "michiel.jpg"})
    assert response.status_code == 200
    assert response.json() == "Manager successfully created!"


def test_post_regio():
    response = requests.post('http://127.0.0.1:8000/regios/',
                             json={"id": 1, "regionaam": "Afrika", "foto": "afrika.jpg", "manager_id": 1})
    assert response.status_code == 200
    assert response.json() == "Regio successfully created!"

def test_post_dier():
    response = requests.post('http://127.0.0.1:8000/dieren/',
                                 json={"id": 1, "diersoort": "Leeuwen", "hoeveelheid": 20, "foto": "leeuwen.jpg", "regio_id": 1})
    assert response.status_code == 200
    assert response.json() == "Dier successfully created!"

def test_get_managers():
    response = requests.get('http://127.0.0.1:8000/managers/')
    assert response.status_code == 200
    managers = response.json()
    for manager in managers:
        assert "id" in manager
        assert "voornaam" in manager
        assert "achternaam" in manager
        assert "manager_nummer" in manager
        assert "foto" in manager


def test_get_manager():
    response = requests.get('http://127.0.0.1:8000/managers/M01')
    assert response.status_code == 200
    manager = response.json()
    assert "id" in manager
    assert "voornaam" in manager
    assert "achternaam" in manager
    assert "manager_nummer" in manager
    assert "foto" in manager


def test_get_regios():
    response = requests.get('http://127.0.0.1:8000/regios/')
    assert response.status_code == 200
    regios = response.json()
    for regio in regios:
        assert "id" in regio
        assert "regionaam" in regio
        assert "foto" in regio
        assert "manager_id" in regio


def test_get_regio():
    response = requests.get('http://127.0.0.1:8000/regios/Afrika')
    assert response.status_code == 200
    regio = response.json()
    assert "id" in regio
    assert "regionaam" in regio
    assert "foto" in regio
    assert "manager_id" in regio


def test_get_dieren():
    response = requests.get('http://127.0.0.1:8000/dieren/')
    assert response.status_code == 200
    dieren = response.json()
    for dier in dieren:
        assert "id" in dier
        assert "diersoort" in dier
        assert "foto" in dier
        assert "regio_id" in dier


def test_get_dier():
    response = requests.get('http://127.0.0.1:8000/dieren/Leeuwen')
    assert response.status_code == 200
    dier = response.json()
    assert "id" in dier
    assert "diersoort" in dier
    assert "foto" in dier
    assert "regio_id" in dier


def test_get_dier_by_regio():
    response = requests.get('http://127.0.0.1:8000/dier/1')
    assert response.status_code == 200
    dieren = response.json()
    for dier in dieren:
        assert "id" in dier
        assert "diersoort" in dier
        assert "foto" in dier
        assert "regio_id" in dier


def test_put_manager():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.put('http://127.0.0.1:8000/managers/M01',
                            json={"id": 1, "voornaam": "Sammie", "achternaam": "Stege", "manager_nummer": "M01", "foto": "sammie.jpg"},
                            headers=headers)
    assert response.status_code == 200


def test_put_regio():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.put('http://127.0.0.1:8000/regios/Afrika',
                            json={"id": 1, "regionaam": "Azië", "foto": "azie.jpg", "manager_id": 1},
                            headers=headers)
    assert response.status_code == 200


def test_put_dier():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.put('http://127.0.0.1:8000/dieren/Leeuwen',
                            json={"id": 1, "diersoort": "Leeuwen", "hoeveelheid": 25, "foto": "leeuwen.jpg", "regio_id": 1},
                            headers=headers)
    assert response.status_code == 200


def test_delete_manager():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete('http://127.0.0.1:8000/managers/M01', headers=headers)
    assert response.status_code == 200
    assert response.json() == "Manager successfully deleted!"


def test_delete_regio():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete('http://127.0.0.1:8000/regios/Azië', headers=headers)
    assert response.status_code == 200
    assert response.json() == "Regio successfully deleted!"


def test_delete_dier():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete('http://127.0.0.1:8000/dieren/Leeuwen', headers=headers)
    assert response.status_code == 200
    assert response.json() == "Dier successfully deleted!"


def test_delete_eigenaar():
    access_token = test_post_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.delete('http://127.0.0.1:8000/eigenaar/test', headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.json() == "Eigenaar successfully deleted!"
