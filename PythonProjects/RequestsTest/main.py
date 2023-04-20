import requests

response = requests.post('https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": "2f5fe0ec8a35b2e60e09089e381d0fa1",
    "email": "asdf@mail.ru",
    "password": "Iloveqa1"
})
print(response.text)

token = '2f5fe0ec8a35b2e60e09089e381d0fa1'


response_activated = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
})
print(response.text)

host = 'https://pokemonbattle.me:9104'


'''response_new_pokemon = requests.post(f'{host}/pokemons', headers = {'trainer_token' : token}, json={
    "name": "Олежка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_new_pokemon.text)'''


'''response_change_name = requests.put(f'{host}/pokemons', headers = {'trainer_token' : token}, json={
    "pokemon_id": "9372",
    "name": "Стасик",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response_change_name.text)'''

response_add_pokemon_in_pokeball = requests.post(f'{host}/trainers/add_pokeball', headers = {'trainer_token' : token}, json={
    "pokemon_id": "9372"
})
print(response_add_pokemon_in_pokeball.text)