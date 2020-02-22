import json
import requests
from requests.auth import HTTPBasicAuth
from Logs import create_logger

logger = create_logger(__name__)


class RestClient:
    def __init__(self, shoper_url):
        self.shoper_url = shoper_url

    def get_token(self, login, password):
        r = requests.post('https://{}/webapi/rest/auth/'.format(self.shoper_url), auth=HTTPBasicAuth(login, password))
        logger.info('{}: Status CODE {}'.format(self.shoper_url, r.status_code))
        if r.status_code == 200:
            access_token = json.loads(r.text)['access_token']
            logger.info('{}: Access token: {}'.format(self.shoper_url, access_token))
            return access_token
        else:
            logger.warning('{}: {}, {}'.format(self.shoper_url,
                                               json.loads(r.text)['error'],
                                               json.loads(r.text)['error_description']
                                               ))
            return None

    def get_id_parcel(self, token, shipping_id, order_id):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        data = {
            "shipping_id": shipping_id,
            "order_id": order_id
        }
        r = requests.post('https://{}/webapi/rest/parcels'.format(self.shoper_url),
                          headers=headers,
                          data=json.dumps(data)
                          )
        response = self.response_checker(r, 'ID Parcel')
        return response

    def set_shipping_code(self, token, id_parcel, shipping_code, sent=1):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        data = {
            "shipping_code": shipping_code,
            "sent": sent
        }
        r = requests.put('https://{}/webapi/rest/parcels/{}'.format(self.shoper_url, id_parcel),
                         headers=headers,
                         data=json.dumps(data)
                         )

        response = self.response_checker(r, 'Shipping code')
        return response

    def response_checker(self, response, func_name):
        status_code = response.status_code
        if status_code == 200:
            resp = json.loads(response.text)
            logger.info('{}: {} {}'.format(self.shoper_url, func_name, resp))
            return resp
        else:
            error = error_desc = json.loads(response.text)['error']
            error_desc = json.loads(response.text)['error_description']
            logger.warning('{}: {} ERROR: {}, {}: {}'.format(self.shoper_url, func_name,
                                                   response.status_code,
                                                   error, error_desc))
            return {
                'status_code': response.status_code,
                'message': error_desc
            }
