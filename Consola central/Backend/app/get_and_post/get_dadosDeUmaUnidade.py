import requests

Undade_id = 13 #variavel a subestituir pelo 13
url = 'http://127.0.0.1:8000/Dados/13'

dados_data = {
    #"name": "nome valido",
    #"password": "senha valida",
    #"email": "email_valido@gmail.com"
}

response = requests.get(url, json=dados_data)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print('Status code', response.status_code)
    print('Reason', response.reason)
    #print('Reason', response.text)
    #print('JSON', response.json()) OU
    response_data = response.json()
    print(response_data)
    #print(response_data['Username'])
    #print(response_data['email'])
else:
    #erros
    print('Status code', response.status_code)
    print('Reason', response.reason)
    print('Reason', response.text)