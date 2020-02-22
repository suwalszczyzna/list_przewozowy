import json
import requests
from requests.auth import HTTPBasicAuth


class RestClient:
    def __init__(self, shoper_url):
        self.shoper_url = shoper_url

    def get_token(self, login, password):
        r = requests.post('https://{}/webapi/rest/auth/'.format(self.shoper_url), auth=HTTPBasicAuth(login, password))
        if r.status_code == 200:
            return json.loads(r.text)['access_token']
        else:
            raise Exception(r.status_code,
                            json.loads(r.text)['error'],
                            json.loads(r.text)['error_description']
                            )

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
        j = json.loads(r.text)
        print('get_id_parcel', j)
        return j

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
        j = json.loads(r.text)
        print('set_shipping_code', j)

# jesli utworzono: {'error': 'invalid_request', 'error_description': 'All products has been already sent'}
# jesli nie znaleziono: {'error': 'invalid_request', 'error_description': "Wartość pola 'order_id' jest niepoprawna: Nie znaleziono wartości '99999'"}
