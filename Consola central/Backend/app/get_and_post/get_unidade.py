import requests

unidade_consola = 1 # variavel a colocar em vez do 1
url = 'http://127.0.0.1:8000/Unidades/1/'  

unidade_data = {
    #"name": "nome valido",
    #"password": "senha valida",
    #"email": "email_valido@gmail.com"
}

response = requests.get(url, json=unidade_data)

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