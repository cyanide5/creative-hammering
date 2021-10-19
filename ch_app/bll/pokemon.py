import logging
from ch_app.dll.pokemon import get_pokemon

logger = logging.getLogger(__name__)


def get_pokemon_abilities(pokemon):
    poke_data = get_pokemon(pokemon)
    abilities = poke_data.get("abilities")
    ability_names = []
    for ability in abilities:
        ability_name = ability['ability']['name']
        ability_names.append(ability_name)
    return ability_names

