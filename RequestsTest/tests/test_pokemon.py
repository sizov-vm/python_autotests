import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'мой токен'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '47436'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_name():
    response_name = requests.get(url = f'{URL}/trainers/{TRAINER_ID}')
    assert response_name.json()['trainer_name'] == 'F1g'