import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'мой токен'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

# Создаие покемона
POKEMON_BODY = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = POKEMON_BODY )
print(response.text)

# Смена имени покемона
RENAME_BODY = {
    "pokemon_id": "1296317",
    "name": "ВАСЯ",
    "photo_id": 2
}
response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = RENAME_BODY)
print(response.text)

# Поймать покемона в покебол
CATCH_BODY = {
    "pokemon_id": "1296317"
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = CATCH_BODY)
print(response.text)

# Получение списка тренеров
TRAINER_ID = '47436'

response = requests.get(url = f'{URL}/trainers')
print(response.text)