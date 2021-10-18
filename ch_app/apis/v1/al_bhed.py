import json
import logging
from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse
from ch_app.bll import al_bhed


api = Namespace("v1/al_bhed", description="Translate English to AlBhed")

logger = logging.getLogger(__name__)

@api.route("")
@api.response(200, "you did it!")
@api.response(400, "you fucked it up")
class AlBhed(Resource):
    phrase = api.model("Phrase",
    {"phrase": fields.String(required=True, example="This is a phrase")}
    )
    def get(self):
        logger.info("Initializing Translation")
        try:
            body = json.loads(request.data.decode("utf-8", errors="ignore"))
        except json.JSONDecodeError:
            logger.error("JSON decoder error while parsing the payload")

        if body['phrase']:
            return al_bhed.translate(body['phrase'])


