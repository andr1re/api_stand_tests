import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
#Después de enviar una solicitud y obtener una respuesta, es útil mostrar el cuerpo de esa respuesta en un formato legible, como un diccionario, para analizar mejor los datos.
#1.Obtén la respuesta: en el fragmento de código anterior obtuviste una respuesta del servidor y la guardaste en la variable de response.
#2.Muestra la respuesta como un diccionario: la respuesta que obtienes suele estar en formato JSON. La librería Requests tiene un método json() que convierte el cuerpo de la respuesta en un diccionario de Python. Agrégalo a tu código.
print(response.json())
#29 nov
