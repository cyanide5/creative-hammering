import json
import logging
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from ch_app.bll import al_bhed
from flask import abort

api = Namespace("v1/al_bhed", description="Translate English to AlBhed")

parser = reqparse.RequestParser()
parser.add_argument('input_type', type=str, required=True, choices=(["eng", "alb"]))
parser.add_argument('input_string', type=str, required=True)

logger = logging.getLogger(__name__)


@api.route('/translate')
@api.response(200, "You did it!")
@api.response(400, "Unsupported request")
class AlBhed(Resource):

    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        logger.info("Initializing Translation")
        if args.get("input_type") == "eng":
            resp = al_bhed.translate_eng(args.get("input_string"))
            return resp
        else:
            abort(400, "Not a supported entry at this time")
