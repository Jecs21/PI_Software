import requests

url = 'http://127.0.0.1:8000/users/'

users_data = {
    "username": "Teste_Final",
    "email": "Teste_Final@TesteFinal.com",
    "password": "TesteFinal12345678"
}

response = requests.post(url, json=users_data)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print('Status code', response.status_code)
    print('Reason', response.reason)
    #print('Reason', response.text)
    #print('JSON', response.json())
    response_data = response.json()
    print(response_data)
    #print(response_data['Username'])
    #print(response_data['email'])
else:
    #erros
    print('Status code', response.status_code)
    print('Reason', response.reason)
    print('Reason', response.text)