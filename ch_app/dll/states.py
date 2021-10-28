import json
import logging
from flask import abort
from ch_app.dll import states_data

logger = logging.getLogger(__name__)

baseurl = "http://www.JailBase.com/api/1/search/?source_id="
