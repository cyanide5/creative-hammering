import logging
from ch_app.dll.pokemon import get_pokemon

logger = logging.getLogger(__name__)


def get_pokemon_abilities(pokemon):
    poke_data = get_pokemon(pokemon)
    abilities = poke_data.get("abilities")
    return abilities

