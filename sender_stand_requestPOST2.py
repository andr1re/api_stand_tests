import configuration
import requests
import data
from sender_stand_requestGET import get_users_table


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         headers=data.headers)  # inserta los encabezados
response = get_users_table()
print(response.status_code)
print(response.json())
#29 nov