import json
import logging

import requests
from flask import abort
from ch_app.dll import states_data

logger = logging.getLogger(__name__)


def get_jailbase(source, firstname, lastname):
    baseurl = "http://www.JailBase.com/api/1/search/"
    url = f'{baseurl}?source_id={source}&first_name={firstname}&last_name={lastname}'
    jail_resp = requests.get(url)
    jail_cont = jail_resp.content
    jail_data = json.loads(jail_cont)
    return jail_data

