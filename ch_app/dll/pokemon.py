import requests
import json
import logging

logger = logging.getLogger(__name__)


def get_pokemon(pokemon):
    poke_url = 'https://pokeapi.co/api/v2/pokemon/'
    if pokemon:
        logger.info(f"SEARCHING POKEMON DATABASE: {pokemon}")
        poke_resp = requests.get(f'{poke_url}{pokemon}')
        poke_cont = poke_resp.content
        pokemon_data = json.loads(poke_cont)
        return pokemon_data

def get_all_pokemon():
    poke_url = 'https://pokeapi.co/api/v2/pokemon/'
    logger.info(f"NO POKEMON SPECIFIED, RETURNING ALL POKEMON")
    poke_resp = requests.get(f'{poke_url}')
    poke_cont = poke_resp.content
    all_pokemon = json.loads(poke_cont)
    return all_pokemon


def get_total_pokemon():
    all_pokemon = get_all_pokemon()
    count = all_pokemon.get('count')
    return count

