import requests
import logging
import json

logger = logging.getLogger(__name__)


def get_quote():
    url = 'https://api.kanye.rest/'
    kr_resp = requests.get(url)
    content = kr_resp.content
    dick = json.loads(content)
    resp = dick.get('quote')
    logger.debug(f'KANYE_REST RETURNED: {resp}')
    return str(resp)

