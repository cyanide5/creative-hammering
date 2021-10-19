import logging
from ch_app.dll.pokemon import _get_pokemon, get_pokemon_list

logger = logging.getLogger(__name__)


def get_abilities(pokemon):
    poke_data = _get_pokemon(pokemon)
    abilities = poke_data.get("abilities")
    ability_names = []
    for ability in abilities:
        ability_name = ability['ability']['name']
        ability_names.append(ability_name)
    return ability_names


def get_type(pokemon):
    poke_data = _get_pokemon(pokemon)
    poke_types = poke_data.get('types')
    ret_types = []
    for p_type in poke_types:
        type_name = p_type['type']['name']
        ret_types.append(type_name)
    return ret_types

def get_pokemon_choices():
    poke_list = get_pokemon_list()
    choices = []
    for pokemon in poke_list:
        poke_name = '"' + pokemon + '"'
        choices.append(poke_name)
    return choices
