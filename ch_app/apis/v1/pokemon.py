import json
import logging
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from ch_app.bll import pokemon
from flask import abort


api = Namespace("v1/pokemon", description="CHANGE_ME")

parser = reqparse.RequestParser()
parser.add_argument('pokemon', type=str, required=True)

logger = logging.getLogger(__name__)


@api.route('/abilities')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class Pokemon(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        logger.info("Initializing Pokemon")
        input_pokemon = args.get("pokemon")
        resp = pokemon.get_pokemon_abilities(input_pokemon)
        return resp

