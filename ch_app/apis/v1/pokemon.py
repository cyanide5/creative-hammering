import json
import logging
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from ch_app.bll.pokemon import get_pokemon_choices, get_type, get_abilities

from flask import abort

logger = logging.getLogger(__name__)

api = Namespace("v1/pokemon", description="CHANGE_ME")

poke_choices = get_pokemon_choices()

parser = reqparse.RequestParser()
parser.add_argument('pokemon', type=str, required=True, choices=poke_choices)



@api.route('/abilities')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class Pokemon(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        logger.info("Initializing Pokemon")
        input_pokemon = args.get("pokemon")
        abilities = get_abilities(input_pokemon)
        return abilities


@api.route('/types')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class Pokemon(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        logger.info("Initializing Pokemon")
        input_pokemon = args.get("pokemon")
        types = get_type(input_pokemon)
        return types
