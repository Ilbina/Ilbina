import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body.copy());
auth_token = response.json()["authToken"]
print(auth_token)
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body, auth_token):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                                 json=kit_body,
                                 headers={
        "Authorization": "Bearer " + auth_token,
        "Content-Type": "application/json"
    })
response = post_new_client_kit(data.kit_body.copy(), auth_token)
print(response.status_code)
print(response.json())