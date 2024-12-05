# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Prueba 2. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene 15 caracteres
#2 dic
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Prueba 3. Preparación
# Función de prueba negativa
def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400

# Comprueba si el atributo "message" en el cuerpo de la respuesta se ve así: "Nombre de usuario incorrecto.
# El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres".
assert (response.json()) ["message"] == "El nombre que ingresaste es incorrecto. "\
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"
# Tercera prueba (error, el parámetro "firstName" contiene un caracter
def test_create_user_1_letter_in_first_name_get_error_response():
    positive_assert("A")

# Prueba 4. Otro error. Esta función llama a negative_assert_symbol
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Prueba 5. No se permiten espacios (en la lista no pero la API sí, uno se guía con la lista de comprobación)
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

# Prueba 6. No se permiten caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",") #Coloca \\ antes de las comillas dobles.
# Así, el intérprete lo reconocerá como parte del string, no como su principio o final.

# Prueba 7. No se permiten números
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Pruebas 8 y 9. Preparación.
# Prueba 8 dice: el parámetro no se pasa en la solicitud
# Prueba 9 dice: se ha pasado un valor de parámetro vacío
#Se crea una función para estas 2 pruebas que recibe el parámetro user_body
def negative_assert_no_first_name(user_body):
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros necesarios"

# Prueba 8. El parámetro no se pasa en la solicitud
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 9. Se ha pasado un valor de parámetro vacío (string vacío)
def test_create_user_empty_first_name_get_error_response():
# El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_first_name(user_body)

# Prueba 10. Se ha pasado otro tipo de parámetro de "firstName"; número
def test_create_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400 # La solicitud devolverá el código de error 500 (aunque, según la lista de comprobación, debería ser 400), pero no te preocupes por eso por ahora.

