
import pytest
from ch_app.dll import pokemon
import logging

logger = logging.getLogger(__name__)


class MockResponse:
    @staticmethod
    def _get_all_pokemon():
        return ["a", "list", "of", "pokemon"]


@pytest.fixture
def mock_response(monkeypatch):

    def test__get_all_pokemon(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(pokemon.get_pokemon_list, "_get_all_pokemon", test__get_all_pokemon)


def test_get_pokemon_list(monkeypatch):
    result = pokemon.get_pokemon_list()
    print(result)
    return result
