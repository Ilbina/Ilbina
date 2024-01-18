import sender_stand_request
import data

# Функция для получения токена пользователя
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

# Функция для изменения значения в параметре name
def get_kit_body(name):
    # Копируем словарь с телом запроса из файла data
    current_kit_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_kit_body["name"] = name
    # Возвращаем новый словарь с нужным значением name
    return current_kit_body

# Функция для позитивной проверки
def positive_assert(kit_body):
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    # Проверяем, что код ответа - 201
    assert kit_response.status_code == 201
    # Проверяем, что имя в созданном наборе соответствует заданному
    assert kit_response.json()["name"] == kit_body["name"]

# Функция для негативной проверки
def negative_assert_code_400(kit_body):
    # В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    # Проверяем, что код ответа - 400
    assert kit_response.status_code == 400


# Тест 1. Создание набора с допустимым количеством символов (1)
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("а")
    positive_assert(kit_body)

# Тест 2. Создание набора с допустимым количеством символов (511)
# Параметр name состоит из 511 символа
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

# Тест 3. Создание набора с недопустимым количеством символов (0)
# Параметр name состоит из 0 символа
def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Тест 4. Создание набора с недопустимым количеством символов (512)
# Параметр name состоит из 512 символа
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Тест 5. Создание набора с допустимыми символами
# Параметр name состоит из английского алфавита
def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

# Тест 6. Создание набора с допустимыми символами
# Параметр name состоит из русского алфавита
def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

# Тест 7. Создание набора с допустимыми символами
# Параметр name состоит из спецсимволов
def test_create_kit_special_symbol_letter_in_name_get_success_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

# Тест 8. Создание набора с допустимыми символами
# Параметр name содержит пробелы
def test_create_kit_speces_letter_in_name_get_success_response():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

# Тест 9. Создание набора с допустимыми символами
# Параметр name содержит цифры
def test_create_kit_numbers_letter_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Тест 10. Создание набора с непереданным параметром
# Параметр name не передан
def test_create_kit_no_name_get_error_response():
    kit_body = ()
    negative_assert_code_400(kit_body)

# Тест 11. Создание набора с неверным типом параметра (число)
# Параметр name - число
def test_create_kit_type_number_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)