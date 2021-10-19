from flask import Flask, Blueprint, has_request_context, request
import logging
import traceback
from flask_restplus import Api
from flask_restplus.apidoc import apidoc
from ch_app.dll import kanye_rest


from ch_app.apis.v1.al_bhed import api as al_bhed_v1

__version__ = '1.11.0'

app = Flask(__name__)
app.config.from_envvar('CH_CONFIG')
logger = logging.getLogger(__name__)

URL_PREFIX = "/creativeHammer"
apidoc.url_prefix = URL_PREFIX
blueprint = Blueprint('api', __name__, url_prefix=URL_PREFIX)
kanye_quote = kanye_rest.get_quote()

api = Api(
    blueprint,
    title="Creative Hammering Microservices",
    version=__version__,
    description=f'Its a service! \n "{kanye_quote}" -Kanye Rest',
    catch_all_404s=True
)

app.register_blueprint(blueprint)

api.add_namespace(al_bhed_v1)