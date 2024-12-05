#30 nov. Creación de autotests a partir de listas de comprobación
import sender_stand_requestPOST2
import data

#El único campo que requiere cambios en todas las comprobaciones es "firstName"
#por lo que no es necesario crear un cuerpo de solicitud independiente para cada prueba
#Es más eficiente modificar el cuerpo de solicitud ya existente en data.py
#Para eso escribe la función get_user_body(name) en create_user_tests

def get_user_body(name): #Esta función tomará un nombre en forma de string como entrada en cada prueba
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

#Tu primer autotest. Creación de un usuario
def test_create_user_2_letter_in_first_name_get_success_responde():
    # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body) #Guarda el resultado de la solicitud para crear un nuevo usuario en la variable user_response

assert user_response.status_code == 201 #comprobar si la respuesta contiene el código 201
assert user_response.json()["authToken"] != "" #Comprobar si la respuesta contiene el campo authToken y si contiene algunos datos

#Ahora a comprobar de que el resultado de la solicitud de recepción de datos de la tabla user_model se guarde en la variable users_table_response
users_table_response = sender_stand_request.get_users_table()
#Escribe el string que debe estar en la respuesta. El caracter \ se utiliza en Python para hacer un salto de línea
str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
#Comprobar si el usuario exista o hay duplicados en la tabla
assert users_table_response.text.count(str_user) == 1

