import sender_stand_request
import data


# Función para cambiar el valor del parámetro "firstName" en el cuerpo de la solicitud
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Prueba 6. El parámetro "firstName" contiene un símbolo especial (Error 400)
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    user_body = get_user_body("\"№%@\"")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400

    # Prueba. El parámetro "firstName" contiene números (Error 400)
    def test_create_user_has_number_in_first_name_get_error_response():
        negative_assert_symbol("123")

        # Función auxiliar para comprobar errores cuando falta el parámetro "firstName"
        def negative_assert_no_firstname(user_body):
            # 1. Guarda el resultado de la solicitud en la variable response
            response = sender_stand_request.post_new_user(user_body)

            # 2. Comprueba si el código de estado de la respuesta es 400
            assert response.status_code == 400

            # 3. Comprueba si el atributo "code" en el cuerpo de respuesta es 400
            assert response.json()["code"] == 400

            # 4. Comprueba si el atributo "message" tiene el texto de error esperado
            assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

            # Prueba 8. El campo "firstName" falta en el cuerpo de la solicitud
            def test_create_user_no_first_name_get_error_response():
                # El cuerpo de la solicitud se copia del archivo data.py
                user_body = data.user_body.copy()
                # Se elimina el parámetro "firstName" del cuerpo
                user_body.pop("firstName", None)
                # Se comprueba la respuesta de error utilizando la función auxiliar
                negative_assert_no_firstname(user_body)

                # Función auxiliar para comprobar errores cuando falta el parámetro "firstName"
                def negative_assert_no_firstname(user_body):
                    # Guarda el resultado de la solicitud en la variable response
                    response = sender_stand_request.post_new_user(user_body)

                    # Comprueba si el código de estado de la respuesta es 400
                    assert response.status_code == 400

                    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
                    assert response.json()["code"] == 400

                    # Comprueba si el atributo "message" tiene el texto de error esperado
                    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

                # Prueba 8. El campo "firstName" falta en el cuerpo de la solicitud
                def test_create_user_no_first_name_get_error_response():
                    # El cuerpo de la solicitud se copia del archivo data.py
                    user_body = data.user_body.copy()
                    # Se elimina el parámetro "firstName" del cuerpo
                    user_body.pop("firstName", None)
                    # Se comprueba la respuesta de error utilizando la función auxiliar
                    negative_assert_no_firstname(user_body)

                    # Prueba 9. El parámetro "firstName" contiene un string vacío
                    def test_create_user_empty_first_name_get_error_response():
                        # El cuerpo de la solicitud actualizada se guarda en la variable user_body
                        user_body = get_user_body("")
                        # Comprueba la respuesta
                        negative_assert_no_firstname(user_body)

                        # Prueba 10. Error
                        # El tipo del parámetro "firstName" es un número
                        def test_create_user_number_type_first_name_get_error_response():
                            # El cuerpo de la solicitud actualizada se guarda en la variable user_body
                            user_body = get_user_body(12)
                            # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
                            response = sender_stand_request.post_new_user(user_body)

                            # Comprobar el código de estado de la respuesta
                            assert response.status_code == 400
