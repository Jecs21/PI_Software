import requests

url = 'http://127.0.0.1:8000/Dados/'

unidade = requests.get('http://127.0.0.1:8000/Unidades/15')
unidade_data = unidade.json()
print(unidade_data)

dados_data = {
    "data_time": "2221-3-21 17:00",
    "data_value": 2,
    "data_Unidade": 13
}

response = requests.post(url, json=dados_data)

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